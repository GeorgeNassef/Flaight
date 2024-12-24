terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    # These values should be provided during terraform init
    # bucket = "your-terraform-state-bucket"
    # key    = "flaight/terraform.tfstate"
    # region = "us-west-2"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "Flaight"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}
