# Django Polls App

A Django web application for creating and voting on polls, with continuous integration and deployment.

<!-- CI/CD Status: Active -->
<!-- Build: Ready for branch protection setup -->

![Build Status](https://github.com/Gohara22/-swe1-app-/workflows/Django%20CI%2FCD/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/Gohara22/-swe1-app-/badge.svg?branch=main)](https://coveralls.io/github/Gohara22/-swe1-app-?branch=main)

## Features

- Create and manage polls
- Vote on poll questions
- View poll results
- Admin interface for managing polls
- Continuous integration with GitHub Actions
- Automated deployment to AWS Elastic Beanstalk

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Gohara22/-swe1-app-.git
   cd -swe1-app-
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Development

### Code Quality

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **Flake8**: Linting
- **Coverage.py**: Test coverage

To check code formatting:
```bash
black --check .
```

To run linting:
```bash
flake8 .
```

To run tests with coverage:
```bash
coverage run --source='.' manage.py test
coverage report
```

### Continuous Integration

The project uses GitHub Actions for CI/CD:

- Runs on every push and pull request to main branch
- Checks code formatting with Black
- Runs Flake8 linting
- Executes test suite with coverage reporting
- Deploys to AWS Elastic Beanstalk on successful builds

## Deployment

The application is automatically deployed to AWS Elastic Beanstalk when changes are pushed to the main branch and all tests pass.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass and code is formatted
5. Submit a pull request

## License

This project is licensed under the MIT License.