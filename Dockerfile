# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /backend

# Copy the current directory contents into the container at /backend
COPY ./backend /backend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat
RUN apt-get update && apt-get install -y netcat-openbsd

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Copy the entrypoint script to the root directory in the container
COPY ./entrypoint.sh /entrypoint.sh

# Ensure the entrypoint script is executable
RUN chmod +x /entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Run the command to start Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "coffeecompass.wsgi:application"]