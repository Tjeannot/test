FROM python:3.9-slim

WORKDIR /app

# Copy requirements file
COPY question_2/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY question_2/dist/ml_toolkit-0.1.0.tar.gz .

RUN pip install ml_toolkit-0.1.0.tar.gz

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "question_2.api:app", "--host", "0.0.0.0", "--port", "8000"] 