## Copilot instructions for Data Infrastructure Insights documentation

### Repository overview
Product: Data Infrastructure Insights

*Data Infrastructure Insights* is a cloud infrastructure monitoring service for hybrid multicloud environments. This repository documents observability, *Storage Workload Security*, Kubernetes monitoring, ONTAP-focused analysis, reporting, APIs, troubleshooting, and vendor-specific data collector integrations.

### Repository structure
- `./` – Primary AsciiDoc content in a flat layout, including onboarding, observability, data collectors, Kubernetes, ONTAP Essentials, Workload Security, reporting, API, troubleshooting, and reference topics.
- `media/` – Shared screenshots, UI images, and diagrams referenced throughout the documentation.
- `media/schemas/` – Reporting schema images used by reporting schema and data model topics.
- `schema/` – Supplemental reporting schema HTML pages referenced by schema table documentation.
- `.github/` – Repository metadata and repository-level Copilot instructions.

### Product-specific context
**Architecture and components:**
- *Tenant* means the customer's Data Infrastructure Insights environment; collectors, dashboards, alerts, APIs, and reporting data are scoped to a tenant.
- *Acquisition Unit (AU)* is a dedicated server or VM that gathers data from infrastructure data collectors and sends it to the tenant.
- *Data collectors* are vendor or service integrations that gather inventory and performance data; the docs distinguish *Infrastructure* collectors from *Service* collectors, which are also called *Integrations*.
- *Telegraf* is the Windows/Linux agent for integration data; it is described as a plugin-driven agent with input plugins that gather metrics, events, and logs and output plugins that send that data to Data Infrastructure Insights.
- *Kubernetes Monitoring Operator* is the Kubernetes collection path; it collects *Cluster Metrics* and can also enable *Network Performance and Map*, *Event Logs*, and *Change Analysis*.
- *Storage Workload Security* uses an agent plus storage collectors and directory services connectors to collect file access and user information for threat detection, forensics, alerting, and automated response.
- *Reporting* uses IBM Cognos Analytics and a *Data Warehouse* populated by *ETL* (Extract, Transform, Load) from Data Infrastructure Insights data.
- *ONTAP Essentials* is a set of dashboards and workflows for ONTAP inventories, workloads, data protection, security, infrastructure, networking, and alerts.

**Key concepts:**
- *Inventory* refers to discovered objects such as storage, switches, virtual machines, or Kubernetes resources; *performance* data is polled separately and summarized over time.
- *Node metrics* are metrics gathered from the server or VM where a Telegraf agent is installed, in addition to any configured service collection.
- *API Access Tokens* grant scoped API access and are passed in the `X-CloudInsights-ApiKey` HTTP header.
- *Feature set roles* can differ by area such as *Observability*, *Workload Security*, and *Reporting*, so API and UI capabilities are role-dependent.
- *Data Warehouse* is the reporting-side stored dataset; *ETL* is the process that extracts collected tenant data, transforms it, and loads it for reporting.

**Naming conventions and terminology:**
- The repository uses the product name *Data Infrastructure Insights*; some topics also note former names such as *Cloud Insights* and *Cloud Secure*.
- The repository uses *AU* for *Acquisition Unit* and *SVM* for *Storage VM*.
- *Workload Security* is the repository term for the security feature set that handles agent-based access monitoring, forensics, and response.
- Kubernetes collection is named *Kubernetes Monitoring Operator* or *NetApp Kubernetes Monitoring Operator*, with optional components named exactly as documented.
- *Data collector* is the standard term for supported source integrations, and vendor/product names are preserved in collector reference topics.

### Typical user workflows
**Observability onboarding:** Create or access a tenant → install an *Acquisition Unit* or *Telegraf*/*Kubernetes Monitoring Operator* path as needed → configure data collectors → allow inventory and performance polling → use dashboards, queries, monitors, and alerts

**Workload Security setup:** Deploy the *Workload Security* agent → add a directory services connector → configure storage data collectors such as ONTAP SVM or Cloud ONTAP → monitor alerts and forensic activity → apply automated response or access restrictions if needed

**Kubernetes monitoring:** Review operator prerequisites → download operator files → adjust proxy or private registry settings if needed → apply the operator to the cluster → analyze cluster, namespace, node, network, event, and change data

**Reporting workflow:** Open *Reporting* → use predefined reports or create custom reports in Cognos → rely on *ETL* to populate the *Data Warehouse* → analyze inventory, capacity, performance, chargeback, or forecasting data
