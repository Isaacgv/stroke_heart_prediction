# Heart Stroke Predictions Model In Production

## Users :
* Medical professionals
* Clinics / hospitals
* Medical devices

## Usage Description:

* After providing the necessary information to the health professionals of the user or inputting his or her personal & health information on the medical device or the Web Interface.
Our model will use the the information provided by the user above to predict the probability of him having a stroke. 
After that the Web interface will display a detailed result about the patient status and possible precautions or advices to visit a professional

## Features:
Our application will feature a :
* Web interface & Data Search Interface using Streamlit
* Prediciton API using FastApi
* Machine Learning Model as Python Package "stroke-pred-p0w11'
* Data Storage unit using PostgresSQl & Sqlalchmey
* Data Ingestion job using Airflow to collect our data based on the user inputs.
* Prediction monitoring dashboard using Gafana

## Dataset: 
* 11 clinical features for predicting stroke events:
https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

## Postgres Database Setup :

1. Make sure to install database dependencies [psycopg2, python-dotenv, sqlalchemy]. <br />
   -Check stroke_heart_prediciton/requirements.txt (Remark For Mac, Linux Users psycopg2-binary) :point_left:
3. Create a (.env) file in the main Root =>  stroke_heart_prediciton/.env
4. (.env) File Should Contain: :exclamation: 
```
[POSTGRES_DB]
POSTGRES_USER=[User]
POSTGRES_PASSWORD=[Password]
POSTGRES_SERVER=[Server]
POSTGRES_PORT=[Port]
POSTGRES_DB=[Database]

[FastApi]
BACKEND_SERVER =[Server]

```
4. Open terminal and go to Cd stroke_heart_prediciton/postgres 
5. Run Python createdb.py to create the tables & relationships in your database

## Airflow ( Follow the steps in Repo )
[Airflow Repo - README.md](https://github.com/Isaacgv/stroke_prediction_airflow#readme)

## Grafana ( Follow the steps in Repo )
[Grafana Repo - README.md](https://github.com/Patrick844/grafana-heroku#readme)

## Execute Program Locally:

1. Cd stroke_heart_prediciton/stroke_api; uvicorn  main:app --host 0.0.0.0 --port 8005;

2. streamlit run web_interface.py --server.port 8010;


![Screenshot 2022-04-27 at 6 56 27 PM](DSP.drawio.png)
