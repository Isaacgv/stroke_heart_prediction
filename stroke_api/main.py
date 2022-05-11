import sys
sys.path.insert(0,'../stroke_prediction')
import pickle
from fastapi import FastAPI, Request
from numpy import int64
import pandas as pd
import random
import test
app = FastAPI()
file = "../models/classifier.pickle"

def make_predicition(details: dict):
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
    details["id"]=1
    for column_name in df_columns:
        prediciton_df.loc[0,column_name]=details[column_name]
    print(prediciton_df)
    print(test.make_prediction(prediciton_df))
    print("success")


@app.post("/")
async def root(request: Request):
    res = await request.json()#{"message": "Hello World"}
    make_predicition(res)
    return res

@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()