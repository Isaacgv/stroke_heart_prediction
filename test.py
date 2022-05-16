import sys
sys.path.insert(0,'../stroke_prediction')
from numpy import int64
import pandas as pd


from stroke_prediction.inference import make_prediction

from fastapi import FastAPI, Request,Response
from pydantic import BaseModel

class Patient(BaseModel):
    first_name : str
    last_name : str
    age: int
    gender: str
    hypertension: str
    heart_disease: str
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status:str
    doctor_name:str
    doctor_last_name:str


app = FastAPI()
file = "../models/classifier.pickle"

@app.get("/")
def read_root():
    return {"message": "I am Alive!"}

@app.get("/prediction")
def get_prediction(data: Patient):
    return {"result": 0}


# interact with FastAPI endpoint
BACKEND ="http://0.0.0.0:8005/"

def get_prediction(features):
    url =BACKEND + "prediction"
    print(url)
    json_features =json.dumps(features)
    print(json_features)
    response = requests.get(url, json=json_features)
    return response

def get_prediction_document(features):
    response = requests.post(BACKEND+"document", data=features.to_json(orient ='index'))
    return response.content


