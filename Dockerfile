# Use the official Airflow image as the base
FROM apache/airflow:2.9.3

# Switch to root to install system dependencies
USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user
USER airflow

# Upgrade pip to a newer version for faster dependency resolution
RUN pip install --no-cache-dir pip==24.0

# Copy and install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt