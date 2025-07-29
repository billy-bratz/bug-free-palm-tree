# bug-free-palm-tree

The repo name is hilarious

## Getting Started

### Requirements

Requires Python 3.13 or later.

setup virtual environment:

```bash

py -3.13 -m venv .venv
```

Activate the virtual environment:

```bash
# On Windows
.\.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application via uvicorn

```bash
uvicorn main:app --reload
```

### Run the Application via Docker

```bash
 docker build -t rps-example-bot .

 docker run -d -p 8000:8000 rps-example-bot
```

## About the Project

Simple FastAPI application that serves as an example of how to get started with making a RPS (Rock, Paper, Scissors) bot.

## Deployment

### via Render.com

1. Navigate to [Render.com](https://render.com), and create an account if you don't have one.
2. Click Add New > Web Service.
3. Connect your GitHub account and select the repository containing this project.

