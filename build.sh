#!/usr/bin/env bash
#build.sh

set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Making migration...."
python manage.py makemigrations

echo "Running migrations..."
python manage.py migrate

echo "Collection static files ....."
python manage.py collectstatic --noinput

echo "Build completed!!"
