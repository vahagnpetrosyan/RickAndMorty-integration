# FastAPI Rick and Morty Integration

This repository demonstrates a  FastAPI application that integrates with the **Rick and Morty API**. It fetches all characters, locations, and episodes data asynchronously and stores them in JSON files. The project uses **Pydantic** for settings, and includes a client to interact with the API.

## Table of Contents

1. [Project Structure](#project-structure)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Configuration](#configuration)  
5. [Running Locally](#running-locally)  
6. [Usage](#usage)  
7. [Docker Setup](#docker-setup)  
8. [License](#license)

---

## Project Structure
- **`app/settings.py`**: Defines environment-based configuration using Pydantic.  
- **`app/rm_client.py`**: Contains the `RickAndMortyClient` class that makes asynchronous HTTP requests to the Rick and Morty API.  
- **`app/rick_and_morty_app.py`**: Contains `RickAndMortyApp`, a class that internally creates a FastAPI app, configures routes, and handles dependency injection.  
- **`app/main.py`**: Minimal entry point that instantiates `RickAndMortyApp` and exposes `app` for Uvicorn (and Docker) to run.  
- **`data/`**: Stores the JSON files that the API writes to.  
- **`requirements.txt`**: Python dependencies.  
- **`Dockerfile`**: Containerization files (optional, for production deployment).


---

## Features

- **Asynchronous HTTPX** calls to the Rick and Morty API, fetching all pages of Characters, Locations, and Episodes.  
- **Class-based** architecture for both the **FastAPI application** and the **client**.  
- **Pydantic**-based configuration for flexibility (e.g., override API base URL via environment variables).  
- **JSON storage** in a `data/` directory (characters.json, locations.json, episodes.json).  
- **Endpoints** for each resource:  
  - `GET /characters`  
  - `GET /locations`  
  - `GET /episodes`  
- **Health-check** endpoint: `GET /health`.

---  

## Installation

1. Ensure you have **Python 3.10+** installed.  
2. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-rickmorty.git
   cd fastapi_rickmorty
   
   python3 -m venv venv
   source venv/bin/activate 
   
   pip install -r requirements.txt  
   ```
   
## Running Locally  
```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The application will be accessible at http://localhost:8000.

* GET /characters – Fetches and stores all characters in data/characters.json.
* GET /locations – Fetches and stores all locations in data/locations.json.
* GET /episodes – Fetches and stores all episodes in data/episodes.json.
* GET /health – A simple health-check endpoint, returns {"status": "ok"}.
## Docker Setup

```bash
  
  docker build -t fastapi-rickmorty:latest .
  docker run -d --name fastapi_rickmorty -p 8000:80 fastapi-rickmorty:latest
```

## Licence

This project is licensed under the MIT License. Feel free to modify and adapt for your use case.