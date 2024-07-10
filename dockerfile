# Use Python 3.10 Alpine base image
FROM python:3.10-alpine

# Set working directory
WORKDIR /code

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install build dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Copy application code
COPY . .

# Command to run the Flask application
CMD ["flask", "run", "--debug"]
