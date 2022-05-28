from pickle import LIST
from wsgiref.util import request_uri
import sys
sys.path.insert(0,'../stroke_prediction')

from stroke_prediction.inference import make_prediction

import pandas as pd

from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from json import dumps
from typing import List

app = FastAPI()

class Patient(BaseModel):
    id: int
    firstname : str
    lastname : str
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level:Optional[float]=0.0
    bmi: Optional[float]=0.0
    smoking_status:str

def make_one_predicition(patient: Patient):
    pd_dict = patient.dict()
    prediciton_df= pd.DataFrame.from_dict([pd_dict])
    prediciton_df.drop(['firstname','lastname'], axis = 1,inplace=True)
    prediction=int(make_prediction(prediciton_df)[0])
    return {"prediction": prediction}

def make_mulitple_predicition(patients: List[Patient]):
    records= [dict(patients[patienindex]) for patienindex in range(len(patients))]
    prediciton_df= pd.DataFrame.from_records(records)
    prediciton_df.drop(['firstname','lastname'], axis = 1,inplace=True)
    prediciton_df["predicition"]=make_prediction(prediciton_df)
    return dumps(prediciton_df.to_dict('index'))
    
@app.get("/")
def read_root():
    return {"message": "We are ready to go !"}

@app.get("/predcit")
async def predict(patient: Patient):
    result= make_one_predicition(patient)
    return result

@app.get("/document")
async def predict_file(patiens: List[Patient]):
    result = make_mulitple_predicition(patiens)
    return result