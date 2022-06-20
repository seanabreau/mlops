# Sean Abreau mlops project

## Requirements

- Docker
- If you have an m1 mac you may need to run "export DOCKER_DEFAULT_PLATFORM=linux/amd64" due to a libpg incompatibility issue. see more here https://stackoverflow.com/questions/62807717/how-can-i-solve-postgresql-scram-authentifcation-problem

## To Run (Docker)

Ensure all requirements above are met.

1. Build: This step involves building docker images using the project files from the top level repo "ml-ops-starter". Run 'docker-compose up -d --build'

## Endpoints

Application contains 3 endpoints see them here:
http://localhost:8000/docs

## Frontend

Interact with the frontend at:
http://localhost:8501
