# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    vim  # Install vim (which includes vi)

# Create the user and group
RUN groupadd -g 1001 appgroup && useradd -r -u 1001 -g appgroup appuser

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Change ownership of the /app directory
RUN chown -R appuser:appgroup /app

# Switch to the new user
USER appuser

# Command to run the application
CMD ["python", "app.py"]
