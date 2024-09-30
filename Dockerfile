# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install dependencies for Tkinter (required for GUI apps)
RUN apt-get update && apt-get install -y python3-tk && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary Python packages
RUN pip install --no-cache-dir random

# Command to run your Python Tkinter app
CMD ["python", "fun_app.py"]
