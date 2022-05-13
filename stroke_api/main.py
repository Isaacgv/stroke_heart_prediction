<<<<<<< HEAD

=======
>>>>>>> 4b4cd442ff939aa35e173927097270e09b80f9e9
import sys
sys.path.insert(0,'../stroke_prediction')
import pickle
from fastapi import FastAPI, Request
from numpy import int64
import pandas as pd
import random
import test
import json
<<<<<<< HEAD

=======
>>>>>>> 4b4cd442ff939aa35e173927097270e09b80f9e9
app = FastAPI()
file = "../models/classifier.pickle"

def make_predicition(details: dict):
    df_columns=['id', 'gender', 'age', 'hypertension', 'heart_disease',
             'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 
             'bmi','smoking_status']

<<<<<<< HEAD

=======
>>>>>>> 4b4cd442ff939aa35e173927097270e09b80f9e9
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
        prediciton_df.loc[0,column_name] = details[column_name]
    print(prediciton_df)
    print(test.make_prediction(prediciton_df))
    print("success")
    return {"result": int(test.make_prediction(prediciton_df)[0])}


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
    df["result"] = test.make_prediction(df)
    print(df)
    return json.dumps(df.to_dict('index'))
    


<<<<<<< HEAD
=======

>>>>>>> 4b4cd442ff939aa35e173927097270e09b80f9e9
@app.post("/")
async def root(request: Request):
    res = await request.json()#{"message": "Hello World"}
    make_predicition(res)
<<<<<<< HEAD

=======
>>>>>>> 4b4cd442ff939aa35e173927097270e09b80f9e9
    print(make_predicition(res))
    return make_predicition(res)

@app.post("/document")
async def root(request: Request):
    res = await request.json()#{"message": "Hello World"}
    return make_predicition_document(res)

@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()