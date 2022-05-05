import streamlit as st
import pandas as pd
import numpy as np



st.title('Stroke Prediction')
#gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status,stroke




gender_list = np.array(["Male", "Female"])
yes_no = np.array(["Yes", "No"])
work_type_lit = np.array(['Private', 'Self employed', 'Govt job', 'children', 'Never worked'])
residence_type_list = np.array(['Urban', 'Rural'])
st.sidebar.write("""## Enter your information""")
form = st.sidebar.form(key='my_form')
first_name = form.text_input(label='First Name')
st.session_state.firstname=first_name
last_name = form.text_input(label='Last Name')
age = form.number_input(label='Age', min_value=0, step=1, max_value=150)
gender = form.radio("Select gender", gender_list)
hypertension = form.number_input(label='Enter Hypertension value', min_value=0.0, step=0.1)
heart_disease = form.radio("Did you had a heart problem in the past ?", yes_no)
ever_married = form.radio("Have you ever been married ?", yes_no)
work_type = form.radio("What is your work type ?", work_type_lit)
residence_type = form.radio("What is your living environment?", residence_type_list)
avg_glucose_level = form.number_input(label='Enter your Average Glucose Level', min_value=0.0, step=0.1)
bmi = form.number_input(label='Enter your body mass index (bmi)', min_value=0.0, step=0.1)
smoking_status = form.radio("Do you smoke ?", yes_no)
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    st.write(first_name)
    st.sidebar.success("information sent successfully ")

