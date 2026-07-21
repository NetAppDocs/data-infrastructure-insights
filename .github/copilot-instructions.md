## Copilot instructions for Data Infrastructure Insights documentation

### Repository overview
Product: Data Infrastructure Insights

TBD: Data Infrastructure Insights makes managing your heterogeneous storage infrastructure a whole lot easier. With AI-powered analysis, you get a clear map of your storage to workload relationships, no matter how complex. Troubleshoot and tackle issues faster with real-time, actionable insights and automated recommendations for improved performance and utilization. It’s all about reducing risks, cutting costs, and keeping your operations running smoothly and efficiently while confidently scaling for the future.

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
- Kubernetes Monitoring: Cluster explorer, workload maps, network performance
- Workload Security: Ransomware detection, forensics, user blocking
- ONTAP Essentials: Specialized NetApp storage dashboards (capacity, performance, data protection, security)
- Infrastructure Analytics: Change analysis, capacity forecasting
- Reporting: Business intelligence, chargeback, trend analysis

**Data Collection:**
- Managed Units (MU): Billing metric based on monitored capacity (TiB)
- Polling Intervals: configurable per collector
- Data Retention: 90 days metrics, 13 months logs/events
- Real-time: Sub-minute updates for critical metrics

**User Roles:**
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

### 1. Install and Configure Acquisition Units and Data Collectors
1. Deploy Acquisition Unit on Linux/Windows server
2. Access DII UI → Admin > Data Collectors → + Data Collector
3. Select vendor/device type from catalog
4. Enter device credentials and connection details
5. Assign to Acquisition Unit and save
6. Verify collector status shows "Collecting"

### 2. Create Monitors and Set Up Alerting
1. Navigate to Observability > Alerts > Monitors → + Monitor
2. Select metric type (performance, log, or anomaly)
3. Define threshold conditions and severity levels
4. Set notification recipients (email/webhook)
5. Save and activate monitor

### 3. Build Dashboards for Specific Use Cases
1. Go to Observability > Explore > Dashboards → + Dashboard
2. Add widgets (line chart, table, gauge, etc.)
3. Select object types and metrics for each widget
4. Apply filters and grouping as needed
5. Arrange layout and save dashboard
6. Share with appropriate user groups

### 4. Troubleshoot Data Collection Issues
1. Check Observability > Collectors → locate failed collector
2. Review error message and "Test Connection" results
3. Verify network connectivity and firewall rules
4. Confirm credentials and permissions are valid
5. Check Acquisition Unit logs if needed
6. Restart collector after fixing issues

### 5. Investigate Security Incidents
1. Navigate to Security > Alerts → select active alert
2. Review alert timeline and affected files/users
3. Check Forensics > Activity for detailed user actions
4. Analyze attack patterns and anomalies
5. Block user access if needed (manual or automated policy)
6. Document findings and remediation steps

### 6. Optimize Storage Capacity and Performance
1. Review ONTAP Essentials > Capacity dashboard
2. Identify volumes/pools approaching capacity limits
3. Check "Time to Full" predictions
4. Use VM Optimization to reclaim unused resources
5. Create monitors for proactive capacity alerts
6. Plan storage expansion or decommissioning

### 7. Plan for Future Infrastructure Needs
1. Access Reporting → run capacity trend reports
2. Analyze growth patterns and Time to Full forecasts
3. Review VM Optimization recommendations
4. Check Infrastructure Health scores
5. Export data for business case/budget planning

### 8. Integrate DII with Other Tools (Webhooks, APIs)
1. For webhooks: Admin > Notifications → + Webhook
2. Configure endpoint URL and authentication
3. Test webhook with sample alert
4. For APIs: Admin > API Access → create API token
5. Review API documentation (Swagger)
6. Implement API calls in automation scripts