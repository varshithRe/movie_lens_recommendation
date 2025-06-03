# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install build dependencies for scikit-surprise
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libatlas-base-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip \
 && pip install scikit-surprise \
 && pip install -r requirements.txt

# Expose the port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
