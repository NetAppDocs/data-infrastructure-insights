## Copilot instructions for Data Infrastructure Insights documentation

### Repository overview
Product: Data Infrastructure Insights

Data Infrastructure Insights makes managing your heterogeneous storage infrastructure a whole lot easier. With AI-powered analysis, you get a clear map of your storage to workload relationships, no matter how complex. Troubleshoot and tackle issues faster with real-time, actionable insights and automated recommendations for improved performance and utilization. It’s all about reducing risks, cutting costs, and keeping your operations running smoothly and efficiently while confidently scaling for the future.

### Repository structure
- `/`- root containing all .adoc files
- `media/`- images and visual assets
- `schema/`- Reporting/Data Warehouse schema documentation and related files

### Product-specific context
**Architecture and components:**
- Cloud Service: Hosted on AWS and Azure (multi-region, multi-tenant)
- On-Premises Components: Acquisition Units and Agents collect data from local infrastructure
- Data Flow: Collectors → Acquisition Units/Agents → DII Cloud Service → User Interface/API
- Data Collectors (100+ supported):
   - Software modules that gather metrics from infrastructure devices
   - Vendors include: VMware, NetApp ONTAP, Kubernetes, AWS, Azure, Dell, HPE, Pure Storage, and more
   - Types: Storage, Compute, Network, Virtualization, Cloud Services
- Acquisition Units:
   - On-premise software that hosts data collectors
   - Supported OS: Windows, Linux (RHEL, Ubuntu, CentOS, Rocky, etc.)
   - Manages polling and data transmission to cloud service
- Kubernetes Monitoring Operator (NKMO):
   - Deploys as Kubernetes operator in target clusters
   - Collects cluster metrics, logs, events, and network performance data
   - Includes telegraf, fluent-bit, and net-observer components
- Workload Security Agents:
   - Monitor ONTAP file access and user activity
   - Components: SVM data collectors, User directory connectors (AD/LDAP)
   - Provides file tampering detection and automated response
- AI Assistant:
   - Intelligent analysis powered by AI
   - Natural language queries about infrastructure, capacity, or performance
   - Multilingual support (12+ languages)

**Key concepts:**
- Observability: Dashboards, queries, monitors, alerts, metrics
- AI Assistant: AI-driven assistance with analyzing, 
- Kubernetes Monitoring: Cluster explorer, workload maps, network performance
- Workload Security: File Tampering detection, forensics, user blocking
- ONTAP Essentials: Specialized NetApp storage dashboards (capacity, performance, data protection, security)
- Infrastructure Analytics: Change analysis, capacity forecasting
- Reporting: Business intelligence, chargeback, trend analysis
- Data Collection: Managed Units (MU): Billing metric based on monitored capacity (TiB)
- Polling Intervals: configurable per collector
- Data Retention: 90 days metrics, 13 months logs/events
- Real-time: Sub-minute updates for critical metrics
- Account Owner: Full administrative access, billing, user management
- Administrator: Configure collectors, create content, manage users
- User: View and create dashboards/queries/monitors
- Guest: Read-only access to dashboards

**Naming conventions and terminology:**
- Acquisition Unit (AU): On-premises software that hosts data collectors. Example: "Install the AU on a Linux VM"
- Agent: Telegraf-based software for integration data collection. Example: "Configure the Kubernetes agent"
- Annotation: User-defined metadata tags on infrastructure objects. Example: "Add 'Tier 1' annotation to production storage"
- Dashboard: Customizable visualization of metrics. Example: "Create a storage performance dashboard"
- Data Collector: Module that gathers data from a specific device/platform. Example: "Add a VMware vSphere data collector"
- Landing Page: Detailed view of a specific infrastructure object. Example: "Navigate to the storage landing page"
- Managed Unit (MU): Billing unit (typically 1 MU = 1 TiB monitored). Example: "Your environment uses 150 MUs"
- Monitor: Alert rule based on metric thresholds or conditions. Example: "Create a latency monitor for storage volumes"
- Query: Data exploration tool for metrics and logs. Example: "Query all volumes above 80% capacity"
- SAN Analyzer: Block storage topology mapper (host-to-LUN paths). Example: "View iSCSI connections in SAN Analyzer"
- VM Analyzer: Virtual machine to storage path analyzer. Example: "Troubleshoot VM performance with VM Analyzer"
- Webhook: HTTP callback for alert notifications. Example: "Configure Slack webhook for critical alerts"
- Workload Map: Kubernetes network topology and traffic visualization. Example: "View pod-to-pod communication in Workload Map"
- SVM (Storage Virtual Machine) - Logical storage container in ONTAP
- Qtree - Logical subdivision of a FlexVol volume
- SnapMirror - ONTAP replication technology
- ARP (Autonomous Ransomware Protection) - ONTAP built-in ransomware detection
- NKMO - NetApp Kubernetes Monitoring Operator
- DaemonSet - Kubernetes workload that runs on every node
- PV/PVC - Persistent Volume / Persistent Volume Claim
- Workload - Deployment, StatefulSet, DaemonSet, or other K8s controller
- DII - Data Infrastructure Insights
- CI - Cloud Insights (legacy name)
- WS - Workload Security
- AU - Acquisition Unit
- DC - Data Collector
- TTF - Time to Full (capacity forecasting)

### Typical user workflows

**Install and Configure Acquisition Units and Data Collectors:** Deploy Acquisition Unit on Linux/Windows server → Deploy Data Collector → Select vendor/device type from catalog → Enter device credentials and connection details → Assign to Acquisition Unit and save → Verify collector status shows "Collecting"

**Create Monitors and Set Up Alerting:** Navigate to Observability > Alerts > Monitors → + Monitor → Select metric type (performance, log, or anomaly) → Define threshold conditions and severity levels → Set notification recipients (email/webhook) → Save and activate monitor

**Build Dashboards for Specific Use Cases:** Go to Observability > Explore > Dashboards → + Dashboard → Add widgets (line chart, table, gauge, etc.) → Select object types and metrics for each widget → Apply filters and grouping as needed → Arrange layout and save dashboard → Share with appropriate user groups

**Troubleshoot Data Collection Issues:** Check Observability > Collectors → Locate failed collector → Review error message and "Test Connection" results → Verify network connectivity and firewall rules → Confirm credentials and permissions are valid → Check Acquisition Unit logs if needed → Restart collector after fixing issues

**Investigate Security Incidents:** Navigate to Security > Alerts → Select active alert → Review alert timeline and affected files/users → Check Forensics > Activity for detailed user actions → Analyze attack patterns and anomalies → Block user access if needed (manual or automated policy) → Document findings and remediation steps

**Optimize Storage Capacity and Performance:** Review ONTAP Essentials > Capacity dashboard → Identify volumes/pools approaching capacity limits → Check "Time to Full" predictions → Use VM Optimization to reclaim unused resources → Create monitors for proactive capacity alerts → Plan storage expansion or decommissioning

**Plan for Future Infrastructure Needs:** Access Reporting → Run capacity trend reports → Analyze growth patterns and Time to Full forecasts → Review VM Optimization recommendations → Check Infrastructure Health scores → Export data for business case/budget planning

**Integrate DII with Other Tools (Webhooks, APIs):** For webhooks: Admin > Notifications → + Webhook → Configure endpoint URL and authentication → Test webhook with sample alert. For APIs: Admin > API Access → Create API token → Review API documentation (Swagger) → Implement API calls in automation scripts