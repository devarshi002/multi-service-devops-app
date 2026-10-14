# Multi-Service DevOps Application

A containerized full-stack web application built using Docker, Docker Compose, Nginx, and Python.

## Architecture

- **Frontend:** HTML, CSS, JavaScript
- **Web Server:** Nginx
- **Backend:** Python HTTP API
- **Containerization:** Docker
- **Orchestration:** Docker Compose
- **Reverse Proxy:** Nginx routes `/api` requests to the backend service

## How It Works

1. The user opens the frontend in a browser.
2. Nginx serves the website.
3. When the user clicks **Fetch Backend Data**, JavaScript sends a request to `/api`.
4. Nginx forwards the request to the Python backend.
5. The backend returns JSON, which the frontend displays.

## Run Locally

Prerequisites: Docker and Docker Compose.

```bash
git clone https://github.com/devarshi002/multi-service-devops-app.git
cd multi-service-devops-app
docker compose up -d --build
```

Open the application at:

`http://localhost:8084`

Test the API:

```bash
curl http://localhost:8084/api
```

Stop the application:

```bash
docker compose down
```

## Skills Practiced

- Docker images and containers
- Dockerfiles
- Docker Compose
- Container networking and service discovery
- Nginx reverse proxy
- REST-style API communication
- Git and GitHub version control

## Author

Devarshi Tambulkar
