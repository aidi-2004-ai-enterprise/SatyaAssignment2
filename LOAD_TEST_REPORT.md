## **LOAD\_TEST\_REPORT.md**

### **1. Test Scenarios**

We performed 4 load tests on the deployed `penguin-api` Cloud Run service:

| Test Type | Users | Duration   | Purpose                                    |
| --------- | ----- | ---------- | ------------------------------------------ |
| Baseline  | 1     | 60 sec     | Measure normal response under minimal load |
| Normal    | 10    | 5 min      | Typical expected production usage          |
| Stress    | 50    | 2 min      | Determine breaking point under heavy load  |
| Spike     | 1→100 | 1 min ramp | Measure sudden load changes                |

---

### **2. Results Summary**

| Test Type    | Requests | Failures | Failure % | Median (ms) | Avg Latency (ms) | Min (ms) | Max (ms) | 90%ile (ms) | 95%ile (ms) | 99%ile (ms) | RPS  | Fail/s |
| ------------ | -------- | -------- | --------- | ----------- | ---------------- | -------- | -------- | ----------- | ----------- | ----------- | ---- | ------ |
| **Baseline** | 24       | 0        | 0%        | 28          | 485.76           | 25       | 11017    | \~31        | 31          | 11000       | 0.4  | 0      |
| **Normal**   | 1468     | 0        | 0%        | 5           | 19.06            | 4        | 2058     | 7           | 8           | 24          | 4.89 | 0      |
| **Stress**   | 2376     | 0        | 0%        | 25          | 26.97            | 19       | 148      | 29          | 31          | 90          | 19.8 | 0      |
| **Spike**    | 29       | 0        | 0%        | 29          | 32.82            | 27       | 116      | 33          | 35          | 120         | 0.5  | 0      |

---

### **3. Observations**

* All tests completed with **zero failures**, demonstrating high reliability.
* The **Baseline test** experienced one very high latency outlier (\~11 seconds), attributable to a cold start on the initial request.
* Under typical production load (**Normal test**), the service responded with very low latency (median 5 ms).
* The **Stress test** with 50 concurrent users maintained consistent sub-30 ms median latency, handling \~20 RPS without degradation.
* The **Spike test** showed that sudden ramp-up to 100 users for a short period did not cause any failures, with latencies staying well below 150 ms.
* Overall, Cloud Run managed scaling and concurrency efficiently, maintaining performance and stability.

---

### **4. Bottlenecks**

* The primary bottleneck observed was the **cold start delay** on the very first request during the Baseline test.
* No other sustained performance issues or resource bottlenecks were detected during high concurrency or sudden load spikes.

---

### **5. Recommendations**

1. **Configure minimum instance count** in Cloud Run to mitigate cold start latency in production.
2. Implement **health checks and warm-up pings** to keep instances ready and responsive.
3. Keep the Docker image **lightweight and optimized** to reduce startup times.
4. Set up **monitoring and alerting** with Cloud Monitoring or Prometheus to detect and respond to performance anomalies early.
5. Consider **load balancing or autoscaling policies** to better handle spikes beyond tested thresholds.

---

### **6. Success Criteria Check**

✅ Tests completed without crashing
✅ Bottlenecks identified and explained
✅ Recommendations provided for improvement
✅ Cloud Run sustained high throughput and low latency under expected and sudden load

---

