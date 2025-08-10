# Penguin Classification API

## Overview

The Penguin Classification API is a RESTful service that classifies penguin species from uploaded images. It leverages a trained machine learning model packaged inside a Docker container and deployed on Google Cloud Run. The API is designed for scalability, reliability, and fast inference to support research and hobbyist use cases.

---

## Setup Instructions

### 1. Local Setup

- Clone the repository:

```bash
git clone https://github.com/yourusername/penguin-classification-api.git
cd penguin-classification-api
Create and activate a Python virtual environment:


python -m venv .venv
# On Linux/macOS
source .venv/bin/activate
# On Windows
.\.venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Run the API locally using Uvicorn:


uvicorn app.main:app --reload
The API will be accessible at http://127.0.0.1:8000.

2. Docker Setup
Build the Docker image:


docker build -t penguin-classification-api .
Run the container locally:


docker run -p 8000:8000 penguin-classification-api
Access API at http://localhost:8000.

3. Deploy to Cloud Run
Authenticate with Google Cloud:


gcloud auth login
gcloud config set project [PROJECT_ID]
Build and submit the container image:


gcloud builds submit --tag gcr.io/[PROJECT_ID]/penguin-classification-api
Deploy to Cloud Run:


gcloud run deploy penguin-classification-api --image gcr.io/[PROJECT_ID]/penguin-classification-api --platform managed --region [REGION] --allow-unauthenticated
The deployment will provide a public URL for the API.

API Documentation
POST /predict
Description:
Classify a penguin species from an image file.

Request:

Content-Type: multipart/form-data

Parameter: file — the image file

Example using curl:


curl -X POST "http://[API_URL]/predict" -F "file=@/path/to/image.jpg"
Response:

json
{
  "species": "Adelie",
  "confidence": 0.98
}
Answers to Reflection Questions
1. What edge cases might break your model in production that aren't in your training data?
Edge cases include images with poor lighting, occlusions, unseen penguin species, very low resolution, or images unrelated to penguins. These may reduce prediction accuracy or cause unexpected behavior.

2. What happens if your model file becomes corrupted?
The service will fail to load the model, causing errors on startup or prediction. Proper error handling and alerting should be implemented, with fallback mechanisms if possible.

3. What's a realistic load for a penguin classification service?
Realistically, around 5 requests per second during peak usage, scaling up as needed for more users or batch jobs.

4. How would you optimize if response times are too slow?
By profiling and optimizing the model, caching results, scaling horizontally, and optimizing preprocessing code.

5. What metrics matter most for ML inference APIs?
Latency, throughput (requests per second), error rate, CPU and memory usage.

6. Why is Docker layer caching important for build speed? (Did you leverage it?)
Layer caching avoids redoing unchanged build steps, speeding up builds. The Dockerfile was structured to maximize caching benefits.

7. What security risks exist with running containers as root?
Root containers risk privilege escalation and host compromise. Running as a non-root user is safer.

8. How does cloud auto-scaling affect your load test results?
Auto-scaling can cause cold start delays when new instances spin up, visible as latency spikes.

9. What would happen with 10x more traffic?
Without scaling, latency and failures would rise. Scaling out instances and optimizing code would be required.

10. How would you monitor performance in production?
Using monitoring tools like Google Cloud Monitoring or Prometheus, with alerts on latency, errors, and resource use.

11. How would you implement blue-green deployment?
Deploy a new version alongside the old, switch traffic gradually, monitor, and rollback if issues occur.

12. What would you do if deployment fails in production?
Rollback to the previous stable version, analyze logs, fix issues, and redeploy.

13. What happens if your container uses too much memory?
The container may be killed by the orchestrator, causing downtime. Proper resource limits and monitoring are necessary.
