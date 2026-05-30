# 🌐 System Design Basics: Core Fundamentals & Patterns

Welcome to the **System Design Basics** showcase! This guide is curated to help engineers, architects, and designers master the building blocks of highly scalable, reliable, and performant distributed systems.

Whether you are preparing for system design interviews, reviewing architectural concepts, or looking for real-world design blueprints, this showcase provides clean, visual, and easy-to-digest deep dives into every fundamental topic.

---

## 🗺️ High-Level System Architecture Roadmap

Before diving into individual terms, let's look at how these fundamental building blocks connect in a modern, production-ready system:

```mermaid
graph TD
    %% Define Styles
    classDef client fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px,color:#01579b;
    classDef routing fill:#efebe9,stroke:#8d6e63,stroke-width:2px,color:#4e342e;
    classDef lb fill:#ede7f6,stroke:#673ab7,stroke-width:2px,color:#311b92;
    classDef app fill:#e8f5e9,stroke:#4caf50,stroke-width:2px,color:#1b5e20;
    classDef data fill:#fff3e0,stroke:#ff9800,stroke-width:2px,color:#e65100;
    
    %% Nodes
    User(("📱 User Client")) -->|1. DNS Query| DNS["🔍 DNS Resolver"]
    User -->|2. Get Static Assets| CDN["⚡ CDN (Edge)"]
    User -->|"3. Dynamic Request (HTTPS)"| LB["⚖️ Load Balancer"]
    
    subgraph App_Layer ["Application & Routing Layer"]
        LB -->|Route traffic| GW["🛡️ API Gateway"]
        GW -->|Auth / Rate Limit| S1["💻 Web Server A (Stateless)"]
        GW -->|Auth / Rate Limit| S2["💻 Web Server B (Stateless)"]
    end
    
    subgraph Data_Layer ["Data & Caching Layer"]
        S1 & S2 -->|Read / Write| Cache[("🚀 In-Memory Cache (Redis)")]
        S1 & S2 -->|Transactional Queries| PrimaryDB[("🗄️ Primary DB (PostgreSQL)")]
        PrimaryDB -->|Asynchronous Replication| ReplicaDB[("📖 Read Replica DB")]
        S1 & S2 -.->|Async Tasks| MQ[("📮 Message Queue (Kafka/RabbitMQ)")]
    end
    
    %% Style Assignments
    class User client;
    class DNS,CDN routing;
    class LB,GW lb;
    class S1,S2 app;
    class Cache,PrimaryDB,ReplicaDB,MQ data;
```

---

## 🗂️ Interactive Index & Learning Pathway

The concepts are grouped into 4 logical modules designed to build upon each other:

| Module | Core Topics | Key Takeaways | Link |
| :--- | :--- | :--- | :--- |
| **01. Scalability & Network** | Scaling, Load Balancers, Protocols | Vertical vs. Horizontal, DNS, L4 vs. L7 LB, TCP vs. UDP | [Explore Module 01 ➔](./01_scalability_network.md) |
| **02. Databases & Caching** | CAP/PACELC, SQL/NoSQL, Caching | Strong vs. Eventual Consistency, Cache-Aside, Replication | [Explore Module 02 ➔](./02_databases_caching.md) |
| **03. Reliability & APIs** | API Styles, Idempotency, Patterns | REST vs. gRPC, Rate Limiting, Circuit Breakers | [Explore Module 03 ➔](./03_reliability_apis.md) |
| **04. System Characteristics** | HA, Throughput, Low Latency | SLA/SLOs, Message Queues, Keep-Alive, Hot/Cold Storage | [Explore Module 04 ➔](./04_system_characteristics.md) |
| **05. Interview Blueprint** | Clarifying, Estimating, Refinement | Ask Clarifying Questions, Back-of-the-envelope, Fix Mistakes | [Explore Module 05 ➔](./05_interview_steps.md) |

---

## 🎯 How to Consume this Showcase

1. **Systematic Learning:** Follow modules `01` through `04` sequentially to build a solid foundation.
2. **Visual Learning:** Study the **Mermaid diagrams** included in each section to understand exactly how packets, data, and requests flow.
3. **Reference Sheet:** Use the markdown files as quick search references for terms during engineering design reviews or mock interviews.
