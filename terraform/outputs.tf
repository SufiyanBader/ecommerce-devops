output "eks_cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}

output "eks_cluster_endpoint" {
  description = "EKS cluster endpoint"
  value       = module.eks.cluster_endpoint
}

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "user_db_endpoint" {
  description = "User service database endpoint"
  value       = aws_db_instance.user_db.endpoint
}

output "product_db_endpoint" {
  description = "Product service database endpoint"
  value       = aws_db_instance.product_db.endpoint
}

output "order_db_endpoint" {
  description = "Order service database endpoint"
  value       = aws_db_instance.order_db.endpoint
}