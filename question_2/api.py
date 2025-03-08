from fastapi import FastAPI, Query
from typing import Optional
import inspect
from ml_toolkit.question2 import (
    generate, 
    learn, 
    predict, 
    statistics
)

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to ML Toolkit API"

@app.get("/functions")
def get_functions():
    # Get all functions from question2.py
    functions = {
        "generate": inspect.getdoc(generate),
        "learn": inspect.getdoc(learn),
        "predict": inspect.getdoc(predict),
        "statistics": inspect.getdoc(statistics)
    }
    return functions

@app.get("/process")
def process(
    n_samples: int = Query(..., description="Number of samples to generate"),
    n_features: int = Query(..., description="Number of features to generate"),
    problem: str = Query(..., description="Type of problem: 'classification' or 'regression'")
):
    # Generate dataset
    X, y = generate(problem=problem, n_samples=n_samples, n_features=n_features)
    
    # Get statistics
    stats = statistics(X, y)
    
    # Train model and get error
    model, error = learn(problem, X, y)
    
    # Make predictions
    predictions = predict(model, problem).tolist()
    
    return {
        "statistics": stats,
        "error_rate": float(error),
        "predictions": predictions
    }

@app.get("/classification/process")
def process_classification(
    n_samples: int = Query(..., description="Number of samples to generate"),
    n_features: int = Query(..., description="Number of features to generate")
):
    return process(n_samples=n_samples, n_features=n_features, problem="classification")

@app.get("/regression/process")
def process_regression(
    n_samples: int = Query(..., description="Number of samples to generate"),
    n_features: int = Query(..., description="Number of features to generate")
):
    return process(n_samples=n_samples, n_features=n_features, problem="regression") 