#!/usr/bin/env python3
"""
Convert Markdown tables to AsciiDoc format in schema_tables_dwh_capacity.adoc
"""

import re

def convert_tables_to_asciidoc(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Step 1: Convert ### headings to === (AsciiDoc level 3 headings)
    content = re.sub(r'^### (.+)$', r'=== \1', content, flags=re.MULTILINE)
    
    # Step 2: Convert --- separators to ''' (AsciiDoc horizontal rules)
    content = re.sub(r'^---$', r"'''", content, flags=re.MULTILINE)
    
    # Step 3: Convert Markdown tables to AsciiDoc tables
    table_pattern = re.compile(
        r'^\| Field \| Type \| Description \|\n'
        r'^\|----+\|----+\|----+\|$',
        re.MULTILINE
    )
    
    content = table_pattern.sub(
        '[cols="1,1,2",options="header"]\n'
        '|===\n'
        '| Field | Type | Description',
        content
    )
    
    # Step 4: Remove trailing pipes from table rows
    content = re.sub(
        r'^\| (.+) \| (.+) \| (.+) \|$',
        r'| \1 | \2 | \3',
        content,
        flags=re.MULTILINE
    )
    
    # Step 5: Add table closing |===
    def add_table_close(match):
        return match.group(0) + '\n|==='
    
    content = re.sub(
        r'(^\| .+ \| .+ \| .+)\n\n(?=\*\*Relationships:\*\*)',
        add_table_close,
        content,
        flags=re.MULTILINE
    )
    
    content = re.sub(
        r"(^\| .+ \| .+ \| .+)\n\n(?=''')",
        add_table_close,
        content,
        flags=re.MULTILINE
    )
    
    content = re.sub(
        r'(^\| .+ \| .+ \| .+)\n\n(?====)',
        add_table_close,
        content,
        flags=re.MULTILINE
    )
    
    if re.search(r'^\| .+ \| .+ \| .+$', content.split('\n')[-1]):
        content += '\n|==='
    
    # Step 6: Convert Relationships lists to proper AsciiDoc bullet lists
    # Replace "- " with "* " after **Relationships:** sections
    lines = content.split('\n')
    result_lines = []
    in_relationships = False
    
    for i, line in enumerate(lines):
        if '**Relationships:**' in line:
            in_relationships = True
            result_lines.append(line)
        elif in_relationships:
            # Check if this is a list item line starting with "- "
            if re.match(r'^- .+', line):
                # Convert to AsciiDoc bullet list format
                result_lines.append(re.sub(r'^- ', '* ', line))
            elif line.strip() == '' or line.startswith("'''") or line.startswith('==='):
                # End of relationships section
                in_relationships = False
                result_lines.append(line)
            else:
                result_lines.append(line)
        else:
            result_lines.append(line)
    
    content = '\n'.join(result_lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Conversion complete!")
    print(f"✓ Input:  {input_file}")
    print(f"✓ Output: {output_file}")

if __name__ == "__main__":
    input_file = "schema_tables_dwh_capacity.adoc"
    output_file = "schema_tables_dwh_capacity_converted.adoc"
    
    try:
        convert_tables_to_asciidoc(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
