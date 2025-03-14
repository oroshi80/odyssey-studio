FROM python:3.9-slim

# Install necessary system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . /app/

# Expose port (if you need it for your Django app)
EXPOSE 8010

# Set the entrypoint for your application (adjust as necessary)
CMD ["gunicorn", "--bind", "0.0.0.0:8010", "odyssey_studio.wsgi:application"]