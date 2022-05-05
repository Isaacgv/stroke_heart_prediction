
import requests
import streamlit as st
import pandas as pd
import numpy as np
import json

# interact with FastAPI endpoint
backend ="http://127.0.0.1:8000/"

def get_prediction(url,features):
    req = requests.post(url, data=json.dumps(features))
    st.write(req.content)


with st.form(key='my_form') as form :
    gender_list = np.array(["Male", "Female"])
    yes_no = np.array(["Yes", "No"])
    work_type_lit = np.array(['Private', 'Self employed', 'Govt job', 'children', 'Never worked'])
    residence_type_list = np.array(['Urban', 'Rural'])
    st.sidebar.write("""## Enter your information""")
    first_name = st.text_input(label='First Name')
    last_name = st.text_input(label='Last Name')
    age = st.number_input(label='Age', min_value=0, step=1, max_value=150)
    gender = st.radio("Select gender", gender_list)
    hypertension = st.number_input(label='Enter Hypertension value', min_value=0.0, step=0.1)
    heart_disease = st.radio("Did you had a heart problem in the past ?", yes_no)
    ever_married = st.radio("Have you ever been married ?", yes_no)
    work_type = st.radio("What is your work type ?", work_type_lit)
    residence_type = st.radio("What is your living environment?", residence_type_list)
    avg_glucose_level = st.number_input(label='Enter your Average Glucose Level', min_value=0.0, step=0.1)
    bmi = st.number_input(label='Enter your body mass index (bmi)', min_value=0.0, step=0.1)
    smoking_status = st.radio("Do you smoke ?", yes_no)
    doctor_name = st.text_input(label='Dc. First Name')
    doctor_last_name = st.text_input(label='Dc. Last Name')
    submit_button = st.form_submit_button(label='Submit')

if submit_button :
    # Create Json object row
    #gender,age,hypertension,heart_disease,ever_married,work_type,
    #Residence_type,avg_glucose_level,bmi,smoking_status,stroke
    myform_json= {"first_name": first_name,
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
                       

    st.write(get_prediction(backend,myform_json))
