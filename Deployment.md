# DEPLOYMENT.md

## Containerization and Deployment Process

This document outlines the steps taken to containerize and deploy the Penguin Classification API using Docker and Google Cloud Run.

---

## 1. Containerization with Docker

- **Dockerfile** was created to containerize the FastAPI application along with its dependencies.
- The base image used is `python:3.9-slim` to keep the image lightweight.
- Dependencies are installed using `pip` inside the container.
- The application listens on port `8000` and uses Uvicorn as the ASGI server.
- Docker layer caching was leveraged by ordering Dockerfile commands to install dependencies before copying the application source code.
- The container runs as a non-root user for security.

**Key Dockerfile commands:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY load_test_report.md .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
2. Building the Docker Image
From the project root directory, run:


docker build -t penguin-classification-api .
This command builds the container image locally, tagging it as penguin-classification-api.

3. Testing Locally
Run the container locally to verify:


docker run -p 8000:8000 penguin-classification-api
Access the API at http://localhost:8000.

4. Pushing to Google Container Registry (GCR)
Authenticate with Google Cloud:


gcloud auth login
gcloud config set project [PROJECT_ID]
Build and submit the image to GCR:


gcloud builds submit --tag gcr.io/[PROJECT_ID]/penguin-classification-api
Replace [PROJECT_ID] with your actual Google Cloud project ID.

5. Deploying to Google Cloud Run
Deploy the container image as a managed Cloud Run service:


gcloud run deploy penguin-classification-api \
  --image gcr.io/[PROJECT_ID]/penguin-classification-api \
  --platform managed \
  --region [REGION] \
  --allow-unauthenticated
Replace [PROJECT_ID] with your Google Cloud project ID.

Replace [REGION] with your preferred Cloud Run region (e.g., us-central1).

Upon success, Cloud Run provides a public HTTPS URL for your API.

6. Issues Encountered and Solutions
Cold Start Latency:
Initial requests experienced latency spikes (~10 seconds).
Solution: Configured minimum instance count in Cloud Run to keep instances warm.

Resource Limits:
Occasional out-of-memory errors under high load.
Solution: Increased CPU and memory allocation in Cloud Run settings.

Authentication:
Ensured --allow-unauthenticated flag was set to allow public access.

7. Final Cloud Run URL
After deployment, the API is accessible at:https://penguin-api-272340541507.northamerica-northeast1.run.app/docs#/default/predict_species_predict_post
