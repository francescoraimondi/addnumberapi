# addnumberapi

DESCRIPTION:

    Flask implementation of a simple API that increments a provided number by 1, following the OpenAPI standard. 
    The application has been packed in a Docker container and a template file for IaC deploy on AWS using ECS Fargate has been also provided.


CONTENT:

    - flask-openapi: folder containing the Flask source code as well as the Dockerfile necessary to build the container image
    - custom_onemore.yaml: file containing the OpenAPI specification
    - template.yaml: CloudFormation template to deploy the service on AWS with ECS FARGATE (**NOTE**: The template requires 2 parameters - the ARN of a self-signed HTTPS certificate already stored on ACM and the ARN of the docker image stored on the ECR repository) 
