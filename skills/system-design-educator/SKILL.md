---
name: system-design-educator
description: "Guidelines and instructions for generating premium, visually stunning, interview-ready system design learning materials."
---

# System Design Educator Skill

This skill guides an AI agent to write industry-leading, visually outstanding system design learning modules specifically optimized for software engineers preparing for FAANG-level system design interviews.

---

## 🏗️ Structural Blueprint

Every system design module generated must follow this strict 7-part structure to provide consistency and deep educational value:

### 1. 💬 Clarifying Questions & Scope Definition (Interviewer Dialogue)
*Before laying out any requirements, always start with a simulated mock-interview dialogue to demonstrate how to actively align with the interviewer.*
- **Questions asked by the Candidate**: Ask about scale, custom features, target demographics, constraints, consistency vs availability tradeoffs.
- **Answers from the Interviewer**: Provide concrete answers that narrow the scope and set up the mathematical parameters for estimations.

### 2. 🎯 Core Requirements & Scale Estimations
*Based on the alignment dialogue, formulate concrete goals.*
- **Functional Requirements**: Core user stories (e.g., "User can input a long URL and get a short alias"). Keep it focused (2-3 main features).
- **Non-Functional Requirements**: System qualities (e.g., ultra-low latency redirection, 99.99% availability, durability of mappings).
- **Back-of-the-Envelope Estimations**: Detailed math. Calculate write throughput, read throughput, storage capacity required over 5 years, memory requirements for caching, and bandwidth constraints. Show all steps clearly.

### 3. 🔌 System Interface & API Design
*Design clean, actionable APIs that would be agreed upon during an interview.*
- Define endpoint methods, paths, request headers, query parameters, JSON payload structures, and expected response status codes.
- Example: REST endpoints (`POST /api/v1/shorten`, `GET /{short_url}`) or gRPC service definitions.

### 4. 🗄️ Database Schema & Data Models
*Choose the right data storage engine and map out schemas.*
- **Database Selection**: Relational vs. NoSQL debate (e.g., PostgreSQL vs. Cassandra/DynamoDB) based on PACELC and CAP theorem trade-offs.
- **Database Schema**: Structured Markdown tables representing the tables/collections, columns, data types, indexes, and primary keys.

### 5. 🗺️ High-Level System Architecture
*Present a clear, premium, bird's-eye view flowchart using Mermaid.*
- **Mermaid Styling Directives**:
  - Use custom HSL or hexadecimal hex colors instead of browser defaults (avoid raw red/blue/green). Use sleek dark slate, mint green, active amber, or elegant purple tones.
  - Structure flow logically: Clients -> Route 53/DNS -> API Gateway -> Microservices / Write path vs Read path -> Redis Cache -> Primary/Replica DBs.
  - Group components using clean `subgraph` borders.

### 6. 🚀 Deep-Dive & Detailed Design
*Address the hard engineering challenges and scaling bottlenecks.*
- Explain unique ID generation algorithms (e.g., Base62 encoding, Distributed Key Generation Service, Snowflake ID).
- Cover read scaling (e.g., caching eviction policies like LRU, read replica synchronization, database sharding/partitioning keys).
- Address system reliability (rate limiting, circuit breakers, security).

### 7. ⚖️ Wrap Up & Trade-off Analysis
*Conclude by summarizing the architectural decisions, articulating trade-offs, and listing future enhancements.*
- **Trade-off Deep Dive**: Focus on architectural compromises made (e.g., eventual consistency vs. strong consistency in read replicas, performance vs. costs).
- **Single Points of Failure (SPOF)**: Identify vulnerabilities and how to mitigate them (e.g., active-active load balancer deployments, database replicas).
- **Operational Excellence**: Detail monitoring, telemetry (Prometheus/Grafana), logs aggregation (ELK), and database backup/restore procedures.

---

## 🎨 Visual & Aesthetic Standards

Failure to follow these visual guidelines will result in substandard educational material. The output must look premium and modern:

1. **GitHub Alert Boxes**: Strategically use `> [!NOTE]`, `> [!TIP]`, and `> [!IMPORTANT]` to call out interview tips, key trade-offs, and critical system bottlenecks.
2. **Clean Markdown Tables**: Use tables for comparisons (e.g., SQL vs. NoSQL, CAP theorem choices).
3. **Advanced Mermaid Flowcharts**: Ensure diagrams are readable, balanced, and visually stunning using custom styles:
   ```mermaid
   %% Example Premium Mermaid Style
   graph TD
       classDef primary fill:#4f46e5,stroke:#312e81,stroke-width:2px,color:#fff;
       classDef secondary fill:#0d9488,stroke:#115e59,stroke-width:2px,color:#fff;
       classDef storage fill:#374151,stroke:#1f2937,stroke-width:2px,color:#fff;
       
       Client("📱 Client"):::primary --> LB("⚖️ Load Balancer"):::secondary
       LB --> DB[("🗄️ PostgreSQL")]:::storage
   ```
4. **No Code/Design Placeholders**: All schemas, API paths, and estimations must be fully written out. No placeholders like `// TODO` or `...` are allowed.
