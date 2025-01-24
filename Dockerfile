# Step 1: Use an official Python runtime as the base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container
COPY . /app

# Step 4: Install Python dependencies
RUN pip install psutil

# Step 5: Specify the command to run your application
CMD ["python", "metrics_monitor.py"]
