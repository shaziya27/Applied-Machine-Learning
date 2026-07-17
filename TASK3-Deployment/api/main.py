from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("../model/churn_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is Running"
    }

@app.get("/predict")
def predict():

    sample_input = np.array([
        [0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,2,29.85,29.85]
    ])

    prediction = model.predict(sample_input)

    return {
        "prediction": int(prediction[0])
    }