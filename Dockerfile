FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y gcc g++ build-essential

# Set workdir
WORKDIR /app

# Copy files
COPY . .

# Install Python packages
RUN pip install --upgrade pip \
 && pip install numpy==1.23.5 \
 && pip install scikit-surprise \
 && pip install -r requirements.txt

# Start command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
