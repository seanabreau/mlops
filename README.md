# api-v1

## Requirements

- FastAPI (Python)
- Docker

## To Run (Docker)

Ensure all requirements above are met. There are 2 steps involved;

1. Build: This step involve build an docker image using the project files. Run `docker build -t apiv1_image .`
2. Run: This step involve creating an instance of the image and running it. Run `docker run -p 8000:8000 --name apiv1_container apiv1_image`

## Endpoints

Application contains the following endpoints:
get data
