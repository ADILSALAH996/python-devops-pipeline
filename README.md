# Python DevOps Pipeline

A beginner-friendly DevOps project demonstrating Python application development, Docker containerization, Git version control, and automated CI/CD using GitHub Actions.

## Features

- Python web application
- Health-check endpoint
- Docker containerization
- Automated testing
- GitHub Actions CI/CD pipeline

## Run Locally

```bash
python app.py
```

Open http://localhost:8000 in your browser.

Health check: http://localhost:8000/health

## Build Docker Image

```bash
docker build -t python-devops-pipeline .
```

## Run Docker Container

```bash
docker run -d --name devops-app -p 8000:8000 python-devops-pipeline
```

## Stop the Container

```bash
docker stop devops-app
```