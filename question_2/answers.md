## Question 2.3
ML Toolkit API

This project provides a FastAPI-based API for machine learning operations including data generation, model training, and predictions.

## Docker Setup and Usage

### Building the Docker Image

To build the Docker image, run the following command from the project root directory:

```bash
docker build -t ml-toolkit-api .
```

### Running the Container

To run the container and map the API port to your local machine, use:

```bash
docker run -p 8000:8000 ml-toolkit-api
```

This command maps port 8000 from the container to port 8000 on your local machine, making the API accessible at `http://localhost:8000`.

### API Endpoints

Once the container is running, you can access:

- API documentation: `http://localhost:8000/docs`
- Base endpoint: `http://localhost:8000/`
- Functions information: `http://localhost:8000/functions`
- Process endpoint: `http://localhost:8000/process`
- Classification process: `http://localhost:8000/classification/process`
- Regression process: `http://localhost:8000/regression/process`

### Stopping the Container

To stop the running container:
1. Find the container ID using `docker ps`
2. Stop it using `docker stop <container_id>` 

## Question 2.4

Which framework/solution can we use if we want to have many asynchronous accesses to the API (multithreading and multiprocessing) ?

We choose to implement a fastAPI server instead of Flask Serer, which is already a great way to deal with a lot of asynchronous process at the same time. If we want to expand the capacity of our server, we would need to multiprocess. This can be done with various frameworks, like gunicorn.