# Model Deployment Using FastAPI and Docker

## Task Information
## INTERNSPARK POWERED BY ALFIDOTECH
**Internship:** Artificial Intelligence

**Task Number:** 3

**Project Title:** Model Deployment Using FastAPI and Docker

## Objective

The objective of this project is to deploy a trained Machine Learning model as a REST API using FastAPI and prepare the application for containerized deployment using Docker.

The deployed API allows users to access customer churn predictions through HTTP requests.

## Model Information

**Model Name:** Customer Churn Prediction Model

**Model Type:** Logistic Regression

**Problem Type:** Binary Classification

**Target Variable:** Churn

Prediction Classes:

* 0 → Customer Retained
* 1 → Customer Churned

## Technologies Used

* Python 3.11
* FastAPI
* Uvicorn
* NumPy
* Scikit-Learn
* Pickle
* Docker
* VS Code
* Anaconda

## Project Workflow

1. Load Trained Model
2. Create FastAPI Application
3. Create Home Endpoint
4. Create Prediction Endpoint
5. Test API Locally
6. Access Swagger Documentation
7. Prepare Docker Configuration

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Customer Churn Prediction API is Running"
}
```

### Prediction Endpoint

```http
GET /predict
```

### Example Request

```http
GET /predict
```

or if you're using query parameters:

```text
http://127.0.0.1:8000/predict
```

### Example Response

```json
{
  "prediction": 1
}
```

## API Documentation

FastAPI automatically generates Swagger documentation.

Swagger URL:

```text
http://127.0.0.1:8000/docs
```

The documentation allows users to test API endpoints directly from the browser.

## Results

### Home Endpoint

API server responded successfully.

### Prediction Endpoint

Sample Prediction Output:

```json
{
  "prediction": 1
}
```

### Interpretation

* 0 → Customer Retained
* 1 → Customer Churned

The API successfully loaded the trained model and generated customer churn predictions.

## Environment Setup

Create and activate the conda environment:

```bash
conda create -n churn_project python=3.11
conda activate churn_project
```

### Package Versions

```bash
pip install fastapi==0.116.1
pip install uvicorn==0.35.0
pip install numpy==2.3.1
pip install scikit-learn==1.7.1


## How to Run

### Step 1

Activate environment:

```bash
conda activate churn_project
```

### Step 2

Navigate to API folder:

```bash
cd api
```

### Step 3

Start FastAPI server:

```bash
uvicorn main:app --reload
```

### Step 4

Open:

```text
http://127.0.0.1:8000
```

### Step 5

Access Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Docker Setup

Build Docker image:

```bash
docker build -t churn-api .
```

Run Docker container:

```bash
docker run -p 8000:8000 churn-api
```

## Project Structure

TASK3-Deployment/
│
├── api/
│   └── main.py
│
├── model/
│   └── churn_model.pkl
│
├── screenshots/
│
├── report/
│
├── Dockerfile
│
└── README.md

## Output

The project generates:

* Customer churn predictions
* REST API responses
* Swagger documentation
* Docker deployment configuration

---

## Author

Shaziya Banu

Alfido Tech AI Internship

## GitHub Repository

https://github.com/yourusername/TASK3-Deployment
