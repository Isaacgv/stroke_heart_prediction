from ftplib import error_temp
from typing import OrderedDict
from matplotlib.font_manager import json_dump
import pandas as pd
import numpy as np

import json
from fastapi.responses import JSONResponse
import requests
import streamlit as st

# interact with FastAPI endpoint
BACKEND ="http://0.0.0.0:8005/"

def get_prediction(features):
    url =BACKEND + "predcit"
    response = requests.get(url, json=json.dumps(features))
    if response.status_code ==200:
        results=response.json()
        prediction = results["prediction"]
        return prediction


def get_prediction_document(features):
    response = requests.post(BACKEND+"document", data=features.to_json(orient ='index'))
    return response.content



# Singular Prediction Page Section
st.title("Heart Stroke Prediction")

# CSS Changes for Side Bar 
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 500px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar.expander("Single Predictions"):
    with st.form(key='my_form' ,clear_on_submit=True):
        gender_list = np.array(["Male", "Female"])
        yes_no = np.array(["Yes", "No"])
        work_type_lit = np.array(['Private', 'Self employed', 'Govt job', 'children', 'Never worked'])
        residence_type_list = np.array(['Urban', 'Rural'])
        first_name = st.text_input(label='First Name')
        last_name = st.text_input(label='Last Name')
        age = st.number_input(label='Age', min_value=0, step=1, max_value=150)
        gender = st.radio("Select your Gender", gender_list)
        hypertension = st.radio("Did you had Hypertension in the past ?", yes_no)
        heart_disease = st.radio("Did you had Heart Problem in the past ?", yes_no)
        ever_married = st.radio("Have you ever been married ?", yes_no)
        work_type = st.radio("What is your Work Type ?", work_type_lit)
        residence_type = st.radio("What is your Living Environment?", residence_type_list)
        avg_glucose_level = st.number_input(label='Enter your Average Glucose Level', min_value=0.0, step=0.1)
        bmi = st.number_input(label='Enter your Body Mass Index (bmi)', min_value=0.0, step=0.,format="%.2f")
        smoking_status = st.radio("Do you Smoke ?", ('smoked','formerly smoked','Unknown'))
        doctor_name = st.text_input(label='Dc. First Name')
        doctor_last_name = st.text_input(label='Dc. Last Name')
        submit_button = st.form_submit_button(label='Predict')

if submit_button :
    myform_json= {  "first_name": first_name,
                    "last_name": last_name,
                    "age" : age,
                    "gender": gender,
                    "hypertension": hypertension,
                    "heart_disease": heart_disease,
                    "ever_married" : ever_married,
                    "work_type": work_type,
                    "Residence_type": residence_type,
                    "avg_glucose_level": avg_glucose_level,
                    "bmi": bmi,
                    "smoking_status": smoking_status,
                    "doctor_name":doctor_name,
                    "doctor_last_name":doctor_last_name
                    }
    
    prediciton = get_prediction(myform_json)
    message = f"{first_name} {last_name} You are at risk of a stroke !" if prediciton == 1 else  "you are safe to slay another day :)"
    message_color = 'red' if prediciton == 1 else  'green'
    st.markdown(f"<h3 style='text-align: left;color:{message_color}'> {(message)} </h3>", unsafe_allow_html=True)
  

# File  Prediction Page Section

with st.sidebar.expander("Upload File for Predictions"):
    with st.form(key="predictions"):
        uploaded_files = st.file_uploader("Choose a CSV file")
        if uploaded_files:
            st.write("filename:", uploaded_files.name)

        submit_button_m = st.form_submit_button("Submit")

        if submit_button_m:
            st.success("File sent")

if submit_button_m :
    data = pd.read_csv(uploaded_files)
    result = json.loads(get_prediction_document(data))
    results_table = pd.read_json(result, orient ='index') 
    st.write(results_table)
