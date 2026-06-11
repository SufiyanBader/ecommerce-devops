# E-Commerce DevOps Platform

Microservices e-commerce backend deployed on AWS EKS with full CI/CD.

## Services
| Service | Tech | Port |
|---|---|---|
| user-service | FastAPI + PostgreSQL | 8001 |
| product-service | FastAPI + MongoDB | 8002 |
| order-service | FastAPI + PostgreSQL | 8003 |
| notification-service | FastAPI + Redis | 8004 |
| api-gateway | Nginx | 80 |

## Stack
- CI/CD: GitHub Actions → AWS ECR → ArgoCD
- IaC: Terraform (EKS, VPC, RDS)
- Orchestration: Kubernetes + Helm
- Observability: Prometheus + Grafana + Loki
