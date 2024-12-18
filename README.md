# Weather App CI/CD Pipeline:1.0.47

This project automates the CI/CD pipeline for a **Weather App** developed in **Python**. It facilitates continuous integration and deployment using **Jenkins**, **Docker**, **Amazon ECR**, and **ArgoCD**. The pipeline ensures an efficient, seamless, and dependable process for managing updates and releases.

---

## Features
- **Automated Build and Test**: Automatically builds and tests code upon each push.
- **Static Code Analysis**: Ensures high-quality code using **SonarQube**.
- **Functional Testing**: Validates application functionality using **Selenium**.
- **Artifact Publishing**: Stores build artifacts in **Amazon ECR**.
- **Kubernetes Deployment**: Deploys the application to **Amazon EKS** clusters using **ArgoCD**.
- **Slack Notifications**: Sends pipeline status updates to Slack.

---

## Prerequisites
To run this pipeline, ensure the following are installed and configured:

- **Jenkins**: Configured with the following plugins:
  - Docker
  - Amazon EC2
  - Cloud Agent
  - Slack
  - Git
- **Docker**: For containerizing the application.
- **Amazon ECR**: For storing Docker images as build artifacts.
- **Amazon EKS**: For deploying the application.
- **ArgoCD**: For managing Kubernetes deployments.
- **SonarQube**: For static code analysis.
- **Selenium**: For functional testing.
- **Slack**: For receiving notifications on pipeline status.

---

## Pipeline Workflow
The pipeline performs the following steps:

1. **Code Checkout**: Jenkins retrieves the latest code from the repository.
2. **Static Analysis**: SonarQube performs a static analysis to maintain code quality.
3. **Build**: Compiles the application code and creates a Docker image.
4. **Testing**: Executes Selenium tests to validate the application's functionality.
5. **Artifact Publishing**: Pushes the Docker image to **Amazon ECR** for storage.
6. **Deployment**: Deploys the application to **Amazon EKS** using **ArgoCD**.
7. **Notifications**: Sends Slack notifications on the pipeline's progress and results.

---

## Technologies Used
This project leverages the following technologies:

- **Jenkins**: For CI/CD automation.
- **Docker**: To containerize the application.
- **Amazon ECR**: For storing Docker images.
- **Amazon EKS**: For Kubernetes-based deployments.
- **ArgoCD**: For GitOps-based Kubernetes deployment.
- **SonarQube**: For static code analysis.
- **Selenium**: For functional testing.
- **Slack**: For sending pipeline status notifications.

---


