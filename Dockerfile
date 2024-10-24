# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pip-tools and compile requirements
RUN pip install pip-tools
RUN pip-compile requirements.in
RUN pip-compile requirements-dev.in

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the run_services.sh script into the container
COPY bin/run_services.sh /app/bin/run_services.sh

# Make the run_services.sh script executable
RUN chmod +x /app/bin/run_services.sh

# Expose the ports the services run on
EXPOSE 8000
EXPOSE 4201

# Command to run the run_services.sh script
CMD ["/app/bin/run_services.sh"]
