#!/bin/bash
# Simple script to test CI steps locally

echo "Testing CI steps locally..."

echo "1. Checking Django system..."
python manage.py check

echo "2. Testing Black formatting..."
black --check .

echo "3. Testing Flake8 linting..."
flake8 .

echo "4. Running tests with coverage..."
coverage run --source='.' manage.py test

echo "5. Generating coverage report..."
coverage report

echo "All CI steps completed successfully!"