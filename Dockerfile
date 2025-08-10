# Use an official Python runtime as a base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first 
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
