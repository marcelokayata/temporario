# Use Python 3.8 slim base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the main script (overridden in docker-compose.yml)
CMD ["python", "src/main.py"]