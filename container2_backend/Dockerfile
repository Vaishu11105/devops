# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for NLPCloud and Flask
RUN apt-get update && apt-get install -y \
    python3-tk \
    curl

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Flask app
EXPOSE 5000

# Command to run the backend Flask app
CMD ["python", "c2_back.py"]
