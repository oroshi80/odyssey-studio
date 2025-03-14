# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose the port Django runs on
EXPOSE 8010

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]
