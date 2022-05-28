from importlib.util import resolve_name
import sys
sys.path.insert(0,'../stroke_prediction')
sys.path.insert(0,'../postgres')

from stroke_prediction.inference import make_prediction

import pandas as pd

from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import Optional
from json import dumps
from typing import List

from database import SessionLocal
import models

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

    class Config:
        # Serialize our sql into json 
        orm_mode= True

db =SessionLocal()

def make_one_predicition(patient: Patient)->dict:
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

@app.get("/patients",response_model=List[Patient],status_code=200)
async def get_all_patients():
    patients= db.query(models.Patient).all() # as json 
    return patients

    
@app.get("/patient/{patient_id}")
async def get_patient(item_id: int):
    pass

@app.post("/patients",response_model=Patient,
          status_code=status.HTTP_201_CREATED)
async def create_patient(patient: Patient):
    new_patient =models.Patient(
        firstname=patient.firstname,
        lastname=patient.lastname,
        gender=patient.gender,
        age=patient.age,
        hypertension=patient.hypertension,
        heart_disease=patient.heart_disease,
        ever_married=patient.ever_married,
        work_type=patient.work_type,
        Residence_type=patient.Residence_type,
        avg_glucose_level=patient.avg_glucose_level,
        bmi=patient.bmi,
        smoking_status=patient.smoking_status
    )
    db.add(new_patient)
    db.flush()
    db.commit()
    db.refresh()
    return new_patient 