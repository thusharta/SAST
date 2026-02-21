# Static Application Security Testing (SAST) on Azure DevOps CI/CD

## Project Overview
This repository demonstrates the implementation of **Static Application Security Testing (SAST)** within a **cloud-based CI/CD pipeline** using **Azure DevOps**.  
The project integrates **SonarQube** and **Semgrep** to automatically detect security vulnerabilities, code quality issues, and misconfigurations during the build process.

This work was completed as part of my **Master’s degree capstone / industry project**, with a focus on **secure software delivery and DevSecOps practices**.

---

## Objectives
- Integrate SAST tools into CI/CD pipelines
- Detect vulnerabilities early in the development lifecycle
- Improve code quality and security visibility
- Automate security checks using YAML pipelines
- Align development with DevSecOps best practices

---

## Tools & Technologies Used
- **Azure DevOps** – CI/CD pipeline orchestration
- **SonarQube** – Code quality and security analysis
- **Semgrep** – Static code analysis and security rules
- **Docker** – Containerized services
- **Linux (Ubuntu)** – Build and execution environment
- **YAML** – Pipeline configuration
- **Git** – Version control

---

## Pipeline Workflow
1. Source code is pushed to the repository
2. Azure DevOps pipeline is triggered
3. Build environment is prepared on Ubuntu VM
4. SonarQube analysis is executed
5. Semgrep security scan is performed
6. Reports are generated and published
7. Pipeline fails or passes based on security thresholds

---

## Security Checks Performed
- Code quality analysis
- Detection of hardcoded secrets
- Identification of insecure configurations
- Vulnerability scanning (OWASP-style issues)
- Best-practice violations

---

## Key Learnings
- Hands-on experience with DevSecOps pipelines
- Understanding of SAST tools and their integration
- Troubleshooting CI/CD runtime and permission issues
- Managing Java version compatibility for SonarQube
- Improving pipeline stability and reliability

---

## Repository Contents
- Azure DevOps YAML pipeline files
- SonarQube configuration files
- Semgrep rules and scan outputs
- Documentation of issues identified and fixes applied

---

## Relevance to Industry Roles
This project demonstrates skills relevant to:
- IT Operations & Infrastructure roles
- DevSecOps / Security Engineering (entry-level)
- CI/CD and Cloud Support roles
- Managed Services environments

---

## Notes
This project is intended for **learning and demonstration purposes** and follows industry-aligned DevSecOps practices.  
The setup reflects **real-world CI/CD security integration** in enterprise environments.
