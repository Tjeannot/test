# ML Toolkit

A simple machine learning toolkit for classification and regression tasks.

## Features

- Classification using Linear Discriminant Analysis
- Regression using Linear Regression
- Custom Ordinary Least Squares Regression implementation
- Dataset generation and analysis tools
- Statistical analysis and correlation computation

## Installation

```bash
pip install ml_toolkit
```

## Usage

```python
from ml_toolkit import MLToolkit

# Generate classification dataset
X, y = MLToolkit.generate("classification", n_samples=100, n_features=5)

# Train a model
model, error = MLToolkit.learn("classification", X, y)

# Make predictions
predictions = MLToolkit.predict(model, "classification")

# Get dataset statistics
stats = MLToolkit.statistics(X, y)
```

## Requirements

- numpy
- scikit-learn
- matplotlib

## License

This project is licensed under the MIT License. 