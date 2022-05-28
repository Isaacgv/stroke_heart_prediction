import pandas as pd
import numpy as np
import json

from pydantic import NoneBytes
import requests
import streamlit as st

# interact with FastAPI endpoint
BACKEND ="http://0.0.0.0:8005/"

def get_prediction():
    features= details_to_json()
    url =BACKEND + "predcit"
    response = requests.get(url, json=features)
    if response.status_code ==200:
        results=response.json()
        prediction = results["prediction"]
        return prediction
    else:
        st.error("An error occurred while getting the prediction!")

def color_neg(val):
    color = 'red' if type(val) == str and val=="Risk of Stroke" else 'green'
    return 'color: %s' %color

# Json Encoder doesnt like to deal with Nan's in Float columns
def fix_Column_with_Nan_float(data):
    float_cols = data.select_dtypes(include=['float64','int64']).columns
    str_cols = data.select_dtypes(include=['object']).columns
    data.loc[:, float_cols]=data.loc[:, float_cols].fillna(0.0)
    data.loc[:, str_cols]=data.loc[:, str_cols].fillna('')
    return data

def get_prediction_document(data :pd.DataFrame):
    data=fix_Column_with_Nan_float(data)
    df_json= data.to_dict(orient='records')
    url =BACKEND + "document"
    response = requests.get(url, json=df_json)
    if response.status_code == 200:
        result = json.loads(response.content)
        prediction_df = pd.read_json(result, orient ='index') 
        data["predicition"]=prediction_df["predicition"]
        data["predicition"] = data["predicition"].apply(lambda x:"Risk of Stroke" if x == 1 else "Normal")
        st.dataframe(data.style.applymap(color_neg,subset=['predicition']))
    else:
        st.error("An error occurred while parsinf the file's predictions !")


def details_to_json():
    myform_json= {  "id" :0,
                    "firstname": first_name,
                    "lastname": last_name,
                    "gender": gender,
                    "age" : age,
                    "hypertension": 1 if hypertension=="yes" else 0,
                    "heart_disease": 1 if heart_disease=="yes" else 0,
                    "ever_married" : ever_married,
                    "work_type": work_type,
                    "Residence_type": residence_type,
                    "avg_glucose_level": avg_glucose_level,
                    "bmi": bmi,
                    "smoking_status": smoking_status
                    }
    return myform_json


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
        gender = st.radio("Select your Gender", gender_list)
        age = st.number_input(label='Age', min_value=0, step=1, max_value=150)
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
    prediciton = get_prediction()
    message = f"{first_name} {last_name} You are at risk of a stroke !" if prediciton == 1 else  "you are safe to slay another day :)"
    message_color = 'red' if prediciton == 1 else  'green'
    st.markdown(f"<h3 style='text-align: left;color:{message_color}'> {(message)} </h3>", unsafe_allow_html=True)
  
# File  Prediction Page Section

with st.sidebar.expander("Upload File for Predictions"):
    with st.form(key="predictions",clear_on_submit=True) as form:
        uploaded_files = st.file_uploader("Choose a CSV file")
        if uploaded_files:
            st.write("filename:", uploaded_files.name)
        submit_button_m = st.form_submit_button("Submit")
        if submit_button_m:
            st.success("File sent")

if submit_button_m :
    data = pd.read_csv(uploaded_files)
    get_prediction_document(data)



