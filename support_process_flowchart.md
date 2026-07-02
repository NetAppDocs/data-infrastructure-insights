# Support Process Flowchart — New Web-Based Product

```mermaid
flowchart TD
    Start([User has an issue or question]) --> Contact{How does the user<br/>reach support?}
    Contact --> |Web form / in-app| Form[Submit support ticket]
    Contact --> |Email| Email[Email to support inbox]
    Contact --> |Chat / live| Chat[Live chat session]
    Contact --> |Help center| SelfServe[Search help center / FAQ]

    Form --> Triage
    Email --> Triage
    Chat --> Triage

    SelfServe --> ResolvedSelf{Issue resolved?}
    ResolvedSelf --> |Yes| Close[Close case]
    ResolvedSelf --> |No| Triage

    Triage[Triage: categorize & prioritize] --> Severity{Severity / type?}
    Severity --> |Critical / P0| Escalate[Escalate to engineering / on-call]
    Severity --> |Bug / technical| Bug[Create bug ticket → dev team]
    Severity --> |How-to / config| L1[L1 support handles]
    Severity --> |Billing / account| Billing[Billing / account team]

    Escalate --> ResolveEsc[Resolution path]
    Bug --> ResolveEsc
    L1 --> ResolveL1[Attempt resolution]
    Billing --> ResolveBilling[Billing resolution]

    ResolveL1 --> ResolvedL1{Resolved?}
    ResolvedL1 --> |Yes| Close
    ResolvedL1 --> |No| Escalate

    ResolveEsc --> Close
    ResolveBilling --> Close

    Close --> FollowUp[Optional: follow-up survey]
    FollowUp --> End([End])
```

## Simplified view (high level)

```mermaid
flowchart LR
    A([Contact]) --> B(Triage)
    B --> C{Self-serve?}
    C -->|Yes| D[Help / FAQ]
    C -->|No| E[Assisted support]
    E --> F{Resolved?}
    F -->|No| G[Escalate]
    G --> E
    F -->|Yes| H([Close])
    D --> H
```

## Notes

- **Triage**: Assign type (bug, how-to, billing), priority (P0–P2), and owner.
- **Escalation**: Define clear rules (e.g., P0 → on-call, unresolved L1 after X hours → L2).
- **Close**: Confirm with user when possible and record outcome for reporting.
