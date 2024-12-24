# Flaight - Flight Delay Prediction Service

Author: George Nassef

## Overview

Flaight is a machine learning-powered flight delay prediction service that estimates the likelihood of significant delays (>45 minutes) for given flights. The system uses historical flight data and machine learning to provide accurate delay predictions through a REST API.

## System Architecture

The system consists of several key components:

1. **ML Inference Service**: Python-based service that loads a pre-trained model to make delay predictions
2. **REST API**: FastAPI-based REST endpoint that handles prediction requests
3. **Container Infrastructure**: Docker containers managed in Amazon Elastic Container Registry (ECR)
4. **API Gateway**: AWS API Gateway for request routing and API management
5. **Infrastructure**: Terraform-managed AWS infrastructure for reliable deployment

## Directory Structure

```
.
├── README.md
├── src/
│   ├── api/              # FastAPI application
│   ├── ml/               # ML inference code
│   └── utils/            # Utility functions
├── tests/                # Unit and integration tests
├── deployment/
│   ├── terraform/        # Infrastructure as Code
│   └── docker/           # Container configuration
└── requirements.txt      # Python dependencies
```

## Setup and Deployment

### Local Development

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
uvicorn src.api.main:app --reload
```

### AWS Deployment

1. Configure AWS credentials:
```bash
aws configure
```

2. Initialize Terraform:
```bash
cd deployment/terraform
terraform init
```

3. Deploy infrastructure:
```bash
terraform apply
```

4. Build and push Docker image:
```bash
./deployment/docker/build_and_push.sh
```

## API Usage

### Predict Flight Delay

```bash
curl -X POST "https://api.flaight.com/predict" \
     -H "Content-Type: application/json" \
     -d '{"flight_number": "AA123", "date": "2024-01-20"}'
```

Response:
```json
{
    "flight_number": "AA123",
    "date": "2024-01-20",
    "delay_probability": 0.35,
    "prediction_timestamp": "2024-01-19T14:30:00Z"
}
```

## Infrastructure

The system is deployed on AWS using the following services:

- Amazon ECS (Elastic Container Service)
- Amazon ECR (Elastic Container Registry)
- AWS API Gateway
- AWS CloudWatch for logging and monitoring
- AWS IAM for security and access control

The infrastructure is managed using Terraform for reproducible deployments and easy environment management.

## Security

- All API endpoints are secured using API keys
- Container images are scanned for vulnerabilities
- Infrastructure follows AWS security best practices
- Secrets are managed using AWS Secrets Manager

## Monitoring and Logging

- API Gateway metrics and logs
- Container logs in CloudWatch
- Custom metrics for model performance
- Automated alerting for system health

## License

MIT License
