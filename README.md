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

## Limitations

- My repo does not have .env or .secrets, these are important when working with teams and sensitive info.
- The main limitation of my pipeline is scalability. Kubernetes would be a better approach for scale than multiple docker containers.
- Eventually if our database gets large enough we should consider sharding our db, or switching to a non relational db. Right now there is a single point of failure for our systems.
- If speed is important for us we should consider in memory approaches like redis, caching could also help.
- Instead of storing our unprocessed images and processing them in our inference function, we should perhaps store the images already processed in our db.
- Metrics and monitoring is important. Integrating our api with datadog or cloudflare could help our response time and protect our systems. We could also better understand the number of read/write queries per second to better optimize our systems.
- Using sql alchemy or another object relational manager would be a good practice for querying our dbs.

## Task 1

 - Please find task 1 presentation at the top level of the repo "IIP to producuction.pdf"
