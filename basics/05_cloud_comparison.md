# ☁️ Part 5: Cloud Services Comparison Chart

When you build systems in the real world, you don't usually buy physical computers. Instead, you rent them from giant cloud providers. The three biggest cloud providers are:
*   **AWS** (Amazon Web Services)
*   **GCP** (Google Cloud Platform)
*   **Azure** (Microsoft Azure)

Every cloud provider has its own names for the exact same system design tools. This simple cheat sheet maps these tools across the three major clouds so you can talk about them in your interviews and work projects!

---

## 🗺️ The Ultimate Cloud Mapping Table

Here is how the core system design components map across the three major cloud providers:

| System Design Concept | What it does | 🟠 AWS | 🔵 GCP | 🟢 Azure |
| :--- | :--- | :--- | :--- | :--- |
| **DNS** | The phonebook that converts website names (like `google.com`) into computer IP addresses. | Route 53 | Cloud DNS | Azure DNS |
| **CDN** | Cache servers around the world that keep static files close to users for super-fast speeds. | CloudFront | Cloud CDN | Azure Front Door / CDN |
| **Load Balancer** | A traffic cop that splits user requests evenly across your servers to avoid crashes. | ELB / ALB / NLB | Cloud Load Balancing | Azure Load Balancer / Application Gateway |
| **API Gateway** | A front door bouncer that handles rate limits, security, and routes requests to correct services. | API Gateway | API Gateway / Apigee | API Management (APIM) |
| **Compute (Servers)** | Basic virtual computers where your application code actually runs. | EC2 | Compute Engine | Azure Virtual Machines |
| **Serverless Compute** | Runs your code automatically only when a request comes in, so you don't pay for idle servers. | Lambda | Cloud Functions / Cloud Run | Azure Functions |
| **Kubernetes (K8s)** | A manager tool that automatically groups, deploys, and scales containerized servers. | EKS (Elastic Kubernetes Service) | GKE (Google Kubernetes Engine) | AKS (Azure Kubernetes Service) |
| **In-Memory Cache** | Super-fast RAM storage (Redis) to load popular pages in a millisecond. | ElastiCache | Memorystore | Azure Cache for Redis |
| **SQL Database** | Relational databases with strict Excel-style tables and perfect safety. | RDS / Aurora | Cloud SQL / Spanner | Azure SQL / Azure DB for PostgreSQL |
| **NoSQL Database** | Super-fast databases designed to scale across many computers with flexible schemas. | DynamoDB / DocumentDB | Firestore / Bigtable | Cosmos DB |
| **Message Queue** | A background inbox that holds heavy tasks so servers can process them asynchronously. | SQS / SNS / Kinesis | Cloud Pub/Sub | Azure Service Bus / Event Hubs |
| **Cold Storage** | A super cheap offline vault to store old logs and backups that you rarely look at. | S3 Glacier | Cloud Storage (Coldline/Archive) | Azure Blob Storage (Archive Tier) |

---

### Next Module:
👉 [**Part 6: The System Design Interview Blueprint**](./06_interview_steps.md)
