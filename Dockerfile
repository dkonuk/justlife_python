# Use an official Python image as the base
FROM python:3.9-slim

# Install necessary dependencies like Chrome and ChromeDriver
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl wget unzip chromium chromium-driver && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables to prevent Chrome issues
ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_BIN=/usr/bin/chromedriver \
    PORT=5000

# Add a non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Create a working directory in the container
WORKDIR /app

# Copy project files to the container
COPY . .

# Install Python dependencies (make sure requirements.txt exists)
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose a port (useful if your app exposes a service API)
EXPOSE $PORT

# Switch to non-root user
USER appuser

# Default command to run your Selenium application
CMD ["python", "pytest"]