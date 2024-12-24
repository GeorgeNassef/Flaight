variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-west-2"
}

variable "environment" {
  description = "Environment name (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "app_name" {
  description = "Application name"
  type        = string
  default     = "flaight"
}

variable "container_port" {
  description = "Port exposed by the container"
  type        = number
  default     = 8000
}

variable "desired_count" {
  description = "Desired number of container instances"
  type        = number
  default     = 2
}

variable "cpu" {
  description = "CPU units for the container (1 vCPU = 1024)"
  type        = number
  default     = 256
}

variable "memory" {
  description = "Memory for the container in MiB"
  type        = number
  default     = 512
}

variable "health_check_path" {
  description = "Health check path for the API"
  type        = string
  default     = "/health"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "api_key" {
  description = "API key for authentication"
  type        = string
  sensitive   = true
}

variable "domain_name" {
  description = "Domain name for the API (optional)"
  type        = string
  default     = ""
}

variable "enable_auto_scaling" {
  description = "Enable auto scaling for ECS tasks"
  type        = bool
  default     = true
}

variable "min_capacity" {
  description = "Minimum number of tasks when auto scaling is enabled"
  type        = number
  default     = 1
}

variable "max_capacity" {
  description = "Maximum number of tasks when auto scaling is enabled"
  type        = number
  default     = 4
}

variable "ssl_certificate_arn" {
  description = "ARN of SSL certificate for HTTPS (optional)"
  type        = string
  default     = ""
}

variable "enable_waf" {
  description = "Enable AWS WAF for API Gateway"
  type        = bool
  default     = true
}

variable "allowed_ip_ranges" {
  description = "List of allowed IP CIDR ranges"
  type        = list(string)
  default     = []
}

variable "log_retention_days" {
  description = "CloudWatch log retention in days"
  type        = number
  default     = 30
}
