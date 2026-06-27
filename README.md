# E-Commerce DevOps Platform 🚀

A production-grade microservices e-commerce platform built with a complete DevOps pipeline — from code to deployment.

## Architecture Overview

## Tech Stack

| Category | Tools |
|---|---|
| **Languages** | Python 3.11, FastAPI |
| **Containerization** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions |
| **Container Registry** | Docker Hub |
| **Orchestration** | Kubernetes |
| **Package Manager** | Helm |
| **IaC** | Terraform (AWS EKS, VPC, RDS) |
| **Monitoring** | Prometheus, Grafana |
| **API Gateway** | Nginx |
| **Databases** | PostgreSQL, Redis |

## Microservices

| Service | Port | Description |
|---|---|---|
| user-service | 8001 | User registration, JWT authentication |
| product-service | 8002 | Product catalog, inventory |
| order-service | 8003 | Order placement, tracking |
| notification-service | 8004 | Redis-based notification queue |
| api-gateway | 80 | Nginx reverse proxy |

## CI/CD Pipeline

Every push to `main` triggers GitHub Actions which:
1. Installs dependencies for all services
2. Builds Docker images for all 5 services
3. Pushes versioned images to Docker Hub (tagged by git SHA)

## Project Structure

ecommerce-devops/

├── user-service/          # FastAPI + PostgreSQL

├── product-service/       # FastAPI + PostgreSQL

├── order-service/         # FastAPI + PostgreSQL

├── notification-service/  # FastAPI + Redis

├── api-gateway/           # Nginx reverse proxy

├── k8s/                   # Kubernetes manifests

│   ├── user-service/

│   ├── product-service/

│   ├── order-service/

│   ├── notification-service/

│   └── api-gateway/

├── helm/                  # Helm charts

│   └── ecommerce/

├── terraform/             # AWS infrastructure as code

│   ├── vpc.tf             # VPC, subnets, NAT gateway

│   ├── eks.tf             # EKS cluster, node groups

│   ├── rds.tf             # PostgreSQL RDS instances

│   ├── variables.tf

│   └── outputs.tf

├── monitoring/

│   ├── prometheus/        # Metrics scraping + alerting

│   └── grafana/           # Dashboards + datasources

└── .github/

└── workflows/

└── ci.yml         # GitHub Actions pipeline
## Running Locally

### Prerequisites
- Docker Desktop
- Git

### Quick Start

```bash
# Clone the repo
git clone https://github.com/sufiyanbader/ecommerce-devops.git
cd ecommerce-devops

# Start all services
docker compose up --build -d

# Check status
docker compose ps
```

### Service URLs

| Service | URL |
|---|---|
| API Gateway | http://localhost:80 |
| User Service | http://localhost:8001/docs |
| Product Service | http://localhost:8002/docs |
| Order Service | http://localhost:8003/docs |
| Notification Service | http://localhost:8004/docs |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

## Kubernetes Deployment

```bash
# Apply secrets
kubectl apply -f k8s/secrets.yaml

# Deploy all services
kubectl apply -f k8s/user-service/
kubectl apply -f k8s/product-service/
kubectl apply -f k8s/order-service/
kubectl apply -f k8s/notification-service/
kubectl apply -f k8s/api-gateway/
```

### Using Helm

```bash
# Deploy everything with one command
helm install ecommerce helm/ecommerce

# Upgrade deployment
helm upgrade ecommerce helm/ecommerce

# Check status
helm status ecommerce
```

## Infrastructure (Terraform)

```bash
# Initialize Terraform
terraform -chdir=terraform init

# Preview changes
terraform -chdir=terraform plan

# Apply infrastructure
terraform -chdir=terraform apply
```

This provisions on AWS:
- VPC with public and private subnets across 3 AZs
- EKS cluster with auto-scaling node groups (t3.medium)
- RDS PostgreSQL instances for each service
- NAT Gateway for private subnet internet access

## Monitoring

- **Prometheus** scrapes metrics from all services every 15 seconds
- **Grafana** visualizes metrics with pre-configured Prometheus datasource
- **Alerting** rules fire on service downtime, high error rates, slow response times

Grafana login: `admin` / `admin123`

