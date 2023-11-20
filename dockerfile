# Use an official Python runtime as the base image
FROM python:3.9
# Set metadata labels for best practices
LABEL authors="George Pickers"
LABEL org.opencontainers.image.name="Quotamatic"
LABEL org.opencontainers.image.description="Service for monitoring Quota usage in Coralogix"
LABEL org.opencontainers.image.source="https://github.com/georgep1ckers/quotamatic"

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install the required packages
RUN pip install requests \
                chardet \
                charset-normalizer 

# Make port 8081 available to the world outside this container
EXPOSE 8081

# Define the command to run the app using CMD
CMD ["python", "quotamatic.py"]