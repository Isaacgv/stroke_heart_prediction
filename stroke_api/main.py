import sys
sys.path.insert(0,'../stroke_prediction')
import pickle
from fastapi import FastAPI, Request
from numpy import int64
import pandas as pd
import random
from stroke_prediction.inference import make_prediction
from fastapi.responses import JSONResponse
import json
app = FastAPI()
file = "../models/classifier.pickle"

def make_one_predicition(details: json):
    df_columns=['id', 'gender', 'age', 'hypertension', 'heart_disease',
             'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 
             'bmi','smoking_status']

    prediciton_df = pd.DataFrame(columns=df_columns)

    prediciton_df = prediciton_df.astype( dtype={'id' : int, 
                 'gender': object,
                 'age': float,
                 'hypertension': int,
                 'heart_disease': int,
                 'ever_married': object,
                 'work_type': object,
                 'Residence_type': object,
                 'avg_glucose_level': float,
                 'bmi': float,
                 'smoking_status':object})
    details= json.loads(details)
    details["id"]=1
    for column_name in df_columns:
        prediciton_df.loc[0,column_name] = details[column_name]

    prediction=int(make_prediction(prediciton_df)[0])
    return {"prediction": prediction}


def make_predicition_document(details: dict):
    df_columns=['id', 'gender', 'age', 'hypertension', 'heart_disease',
             'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 
             'bmi','smoking_status']

    df = pd.DataFrame.from_dict(details, orient ='index') 
    df = df[df_columns]
    df = df.astype( dtype={'id' : int, 
                 'gender': object,
                 'age': float,
                 'hypertension': int,
                 'heart_disease': int,
                 'ever_married': object,
                 'work_type': object,
                 'Residence_type': object,
                 'avg_glucose_level': float,
                 'bmi': float,
                 'smoking_status':object})
    df["result"] = make_prediction(df)
    print(df)
    return json.dumps(df.to_dict('index'))
    

@app.get("/predcit")
async def root(request: Request):
    res = await request.json()
    result= make_one_predicition(res)
    return result


@app.post("/document")
async def root(request: Request):
    res = await request.json()#{"message": "Hello World"}
    return make_predicition_document(res)

@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()