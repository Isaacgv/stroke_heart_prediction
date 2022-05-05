import pickle
from fastapi import FastAPI, Request
import pandas as pd
import random

app = FastAPI()
file = "../models/classifier.pickle"

def make_predicition(details: dict):
    df_columns=['id', 'gender', 'age', 'hypertension', 'heart_disease',
             'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 
             'bmi','smoking_status']
    prediciton_df = pd.DataFrame(columns=df_columns)
    details["id"]=1
    for column_name in df_columns:
        prediciton_df.loc[0,column_name]=details[column_name]
    
    classifier = pickle.load(open(file, "rb"))
    #print(classifier.predict(prediciton_df))
    print("success")


@app.post("/")
async def root(request: Request):
    res = await request.json()#{"message": "Hello World"}
    make_predicition(res)
    return res

@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()