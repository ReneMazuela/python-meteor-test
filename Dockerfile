# Use a minimal base image
FROM python:3.13

# Set working directory
WORKDIR /app

# Copy code and install dependencies
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
