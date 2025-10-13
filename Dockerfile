# Use an official slim Python image as base
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for MySQLdb and clean up to reduce image size
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    curl \
    python3-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Copy dependency list
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire application code
COPY . .

# Expose the default Flask port
EXPOSE 5000

# Add a healthcheck (useful in CI/CD and Docker Compose)
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1

# Command to run the Flask app
CMD ["python", "app.py"]
