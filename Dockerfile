FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . /app/

# Expose the port
EXPOSE 8010

# Run Gunicorn with the Django app
CMD ["gunicorn", "odyssey_studio.wsgi:application", "--bind", "0.0.0.0:8010"]
