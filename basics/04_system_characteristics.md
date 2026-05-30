# ⚖️ Module 04: System Characteristics & Performance Metrics

This module details the key performance goals, measurements, and trade-offs that system architects balance to achieve High Availability (HA), High Throughput, and Low Latency.

---

## 🏎️ 1. Latency vs. Throughput

Engineers must optimize code and infrastructure depending on the primary performance goal of the system.

```mermaid
graph LR
    subgraph Latency ["Latency (Speed)"]
        L("⏱️ Time taken to complete a single transaction.<br>Target: milliseconds (ms).")
    end
    
    subgraph Throughput ["Throughput (Capacity)"]
        T("📊 Number of transactions processed per second (TPS).<br>Target: Requests Per Second (RPS) or QPS.")
    end
```

### The Trade-off
*   **High Throughput, High Latency:** E.g., batch processing bills or video encoding. You process millions of records at once (high throughput), but each individual job takes minutes (high latency).
*   **Low Latency, Low Throughput:** E.g., a real-time gaming server or high-frequency trading desk. Transactions must occur in sub-milliseconds (low latency), but the server cannot process large concurrent batches of queries (low throughput) without increasing delay.

---

## 🏛️ 2. High Availability (HA)

**Availability** measures the percentage of time a system is fully operational and accessible.

### The "Nines" of Availability

| Availability % | Downtime per Year | Downtime per Month | Target Level |
| :--- | :--- | :--- | :--- |
| **99% ("Two Nines")** | 3.65 days | 7.30 hours | Basic website |
| **99.9% ("Three Nines")** | 8.77 hours | 43.83 minutes | standard SaaS platform |
| **99.99% ("Four Nines")** | 52.60 minutes | 4.38 minutes | E-commerce checkout, Banking APIs |
| **99.999% ("Five Nines")** | 5.26 minutes | 26.30 seconds | Telecommunications, cloud infrastructure |

### Key High Availability Strategies
1.  **Redundancy & Failover:**
    *   **Active-Active:** Multiple active nodes handle traffic simultaneously. If one fails, the load balancer redistributes traffic to the surviving active nodes.
    *   **Active-Passive:** A secondary "passive" backup node sits idle. If the "active" node fails, traffic is redirected (failed over) to the passive node.
2.  **Heartbeats:** Periodic signal packets sent between nodes to monitor node health and trigger automatic failovers when a node becomes unresponsive.
3.  **GeoDNS & Global Failovers:** Routing users to different physical data centers globally based on their location or proximity. If an entire AWS region goes offline, GeoDNS automatically re-routes traffic to the nearest healthy region.

```mermaid
graph TD
    subgraph ActiveActive ["Active-Active Failover (Preferred)"]
        LB1("⚖️ Load Balancer") --> S_A("💻 Active Server A")
        LB1 --> S_B("💻 Active Server B")
    end
    
    subgraph ActivePassive ["Active-Passive Failover"]
        LB2("⚖️ Load Balancer") --> S_C("💻 Active Server (Main)")
        S_C -.->|Heartbeat fails| S_D("💤 Passive Server (Standby)")
        LB2 -.->|Failover route| S_D
    end
```

---

## 📊 3. High Throughput

To scale throughput to handle hundreds of thousands of concurrent requests, systems avoid synchronous blockers.

### Asynchronous Processing & Message Queues
Instead of processing long-running operations during the user's request-response lifecycle, applications dump tasks into a **Message Queue** (e.g., Kafka, RabbitMQ) and respond to the user immediately. Background workers pull tasks from the queue asynchronously.

```mermaid
sequenceDiagram
    participant User as Client
    participant App as Web Server
    participant MQ as Message Queue
    participant Worker as Worker Nodes
    
    User->>App: 1. POST /upload-video
    App->>MQ: 2. Enqueue "Process Video" Task
    App-->>User: 3. Return 202 Accepted (Processing...)
    Note over User: Client is unblocked!
    
    MQ->>Worker: 4. Poll & Fetch Task
    Worker->>Worker: 5. Encode video (CPU Intensive)
```

---

## ⚡ 4. Low Latency

Optimizations that minimize the time packets spend traveling or waiting:

1.  **Content Delivery Networks (CDNs):** Distributed networks of servers that cache static assets (images, JS, CSS, video files) at the "edge" of the internet, serving them from physical locations closest to the user.
2.  **Edge Computing:** Running light serverless functions directly on CDN edge servers (e.g., Cloudflare Workers) to process requests without routing them back to the origin database.
3.  **HTTP/3 & QUIC:** Utilizes UDP instead of TCP to eliminate Head-of-Line blocking and drastically decrease connection handshake times.
4.  **Multiplexing & Keep-Alive:** Reusing standard TCP connections for multiple HTTP requests rather than establishing a new connection handshake every time.

---

## ❄️ 5. Hot vs. Cold Storage (Tiered Storage)

To optimize cost while maintaining low latency, architects separate data based on access frequency.

```mermaid
graph TD
    Data("🗃️ System Data") --> Hot("🔥 Hot Storage (Frequent access)")
    Data --> Warm("🌤️ Warm Storage (Occasional access)")
    Data --> Cold("❄️ Cold Storage (Rare access)")
    
    Hot -->|"Redis / SSDs<br>(Fastest, Expensive)"| Out1("⏱️ Sub-millisecond latency")
    Warm -->|"Standard HDD / Relational DB"| Out2("⏱️ Millisecond latency")
    Cold -->|"Amazon S3 Glacier / Tape<br>(Slowest, Extremely Cheap)"| Out3("⏱️ Hours retrieval latency")
```

*   **Hot Data:** User profiles, active sessions, trending feeds. Stored in RAM (Redis) or high-speed NVMe SSDs.
*   **Cold Data:** Logs from 3 years ago, transactional receipts, system backups. Stored in high-latency, extremely low-cost cloud vaults like Amazon S3 Glacier.

---

### Next Module:
👉 [**Module 05: The System Design Interview Blueprint**](./05_interview_steps.md)
