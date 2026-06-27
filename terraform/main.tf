# Main entry point for Terraform configuration
# This file ties together all modules and resources
# defined in vpc.tf, eks.tf, and rds.tf

locals {
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
    Repository  = "github.com/sufiyanbader/ecommerce-devops"
  }
}