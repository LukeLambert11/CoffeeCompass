#!/bin/sh

# Wait for PostgreSQL to start
while ! nc -z db 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

echo "PostgreSQL started"

# Generate database migration files
echo "Generating migration files"
python manage.py makemigrations

# Apply database migrations
echo "Applying database migrations"
python manage.py migrate

# Collect static files (optional)
# echo "Collecting static files"
# python manage.py collectstatic --noinput

# Start the Gunicorn server
echo "Starting Gunicorn"
exec "$@"