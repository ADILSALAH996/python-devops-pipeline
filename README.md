# Python DevOps Pipeline 🚀

A beginner-friendly DevOps project demonstrating Python application development, Docker containerization, automated testing, Git version control, and continuous integration using GitHub Actions.

## 🎯 Project Overview

This project runs a simple Python web application inside a Docker container. A GitHub Actions workflow automatically runs tests, builds the Docker image, and scans it for known security vulnerabilities.

## ✨ Features

- Python HTTP web application
- JSON health-check endpoint
- Docker containerization
- Non-root container user
- Basic container security hardening
- Automated application tests
- GitHub Actions CI pipeline
- Trivy Docker image vulnerability scanning

## 🛠️ Technologies Used

- Python 3.12
- Docker
- Git and GitHub
- GitHub Actions
- Trivy
- Python unittest

## 📁 Project Structure

```text
python-devops-pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
└── test_app.py
```

## ▶️ Run Locally

Ensure Python 3.12 or a compatible Python version is installed.

Start the application:

```bash
python app.py
```

Open the homepage:

http://localhost:8000

Check application health:

http://localhost:8000/health

Expected health-check response:

```json
{
  "status": "healthy",
  "application": "Python DevOps Pipeline"
}
```

Stop the local application with `Ctrl+C` in the terminal running it.

## 🧪 Run Automated Tests

Run the tests with Python's built-in unittest framework:

```bash
python -m unittest discover -v
```

## 🐳 Build the Docker Image

From the project root, run:

```bash
docker build -t python-devops-pipeline .
```

## 🚀 Run the Docker Container

Run the container with the security restrictions used in this project:

```bash
docker run -d --name devops-app -p 127.0.0.1:8000:8000 --read-only --cap-drop=ALL --security-opt=no-new-privileges --tmpfs /tmp:rw,noexec,nosuid,size=16m python-devops-pipeline
```

The application will be available at:

http://localhost:8000

Health check:

http://localhost:8000/health

The port is bound to the local machine rather than all network interfaces.

If a container named `devops-app` already exists, stop and remove it before creating another container with that name:

```bash
docker stop devops-app
docker rm devops-app
```

## ⚙️ Continuous Integration

The GitHub Actions workflow is located at:

`.github/workflows/ci.yml`

It runs when changes are pushed to the `main` branch or when a pull request targets `main`.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Runs automated tests.
4. Builds the Docker image.
5. Scans the image using Trivy.

The Docker image is built for verification but is not published to a container registry by this workflow.

## 🔐 Security Notes

The project applies several basic security measures:

- Runs the application as a non-root user inside Docker.
- Uses a read-only container filesystem.
- Drops Linux capabilities.
- Prevents gaining additional privileges.
- Scans the Docker image for HIGH and CRITICAL vulnerabilities when the workflow runs.

A successful vulnerability scan does not guarantee that an application is completely secure.

## 📌 Current Project Status

- Python application: Implemented
- Docker containerization: Implemented
- Automated tests: Implemented
- GitHub Actions CI: Implemented
- Docker image vulnerability scanning: Implemented
- AWS deployment: Planned

## 🚧 Future Improvements

- Deploy the application to AWS.
- Add application logging and monitoring.
- Publish Docker images to a container registry.
- Introduce a deployment workflow.

## 👨‍💻 Learning Outcomes

This project demonstrates practical experience with Python, Docker, Git, GitHub Actions, automated testing, and basic container security.




## ☁️ AWS EC2 Deployment

### Deployment Overview

The Python DevOps application was successfully deployed to an Ubuntu server on Amazon EC2 using Docker.

**Deployment environment**
- Cloud provider: AWS
- Service: Amazon EC2
- Region: Mumbai (`ap-south-1`)
- Operating system: Ubuntu Server 24.04 LTS
- Containerization: Docker
- Application port: 8000
- Health endpoint: `/health`

### Deployment Steps

1. Launched an Ubuntu EC2 instance.
2. Connected to the instance securely using SSH and a private key.
3. Installed and verified Docker Engine.
4. Transferred the application source files to the server.
5. Built the Docker image on EC2.
6. Ran the container with a read-only root filesystem, dropped Linux capabilities, and other security restrictions.
7. Configured the EC2 security group for application access.
8. Verified the application through a browser and tested the health endpoint.

### Verification

The homepage loaded successfully from the EC2 public address, and the `/health` endpoint returned the expected JSON response.

### Deployment Evidence

Screenshots captured during the deployment are stored in `docs/screenshots/`.

- EC2 instance and status checks
- Successful SSH connection
- Docker installation and test
- Project files on EC2
- Docker image build
- Running container
- Application homepage
- Health-check response
- GitHub Actions workflow

### Cleanup

The temporary EC2 deployment was shut down after testing and documentation. Refer to the AWS console to verify the final instance state and confirm that no unnecessary billable resources remain.

### Lessons Learned

This project provided practical experience with Python, Docker, container hardening, Git, GitHub Actions, automated testing, vulnerability scanning, Linux administration, and AWS EC2 deployment.

### Limitations

- The application uses HTTP rather than HTTPS.
- The CI workflow builds and scans the image but does not publish it or automatically deploy to AWS.
- A successful vulnerability scan does not guarantee complete application security.
