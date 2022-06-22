# Strokes and Heart Failure Predictions Model

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

1. Make sure to install database dependencies [psycopg2, python-dotenv, sqlalchemy],check stroke_heart_prediciton/requirements.txt
( Remark For Mac, Linux Users psycopg2-binary)
2. Create a (.env) file in the main Root =>  stroke_heart_prediciton/.env
3. (.env) File Should Contain:
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

## Execute Program Locally:

1. Cd stroke_heart_prediciton/stroke_api; uvicorn  main:app --host 0.0.0.0 --port 8005;

2. streamlit run web_interface.py --server.port 8010;


![Screenshot 2022-04-27 at 6 56 27 PM](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=DSP#R5Vtdd5s4EP01eYwP4sPgR3%2FEbc6m3XTTc9LsS44CMtYGI1bIid1fv5JBNkiyTRwTJ5s2ac0ghLhzdTUzwmfOcLb4QmE2%2FUYilJzZVrQ4c0Znth10A%2F6vMCwLg2tbhSGmOCpMYGO4wb9RaZTN5jhCea0hIyRhOKsbQ5KmKGQ1G6SUPNebTUhSv2sGY6QZbkKY6NZbHLFp%2BVietbF%2FRTieyjsDqzwzg7JxacinMCLPFZNzceYMKSGs%2BDRbDFEisJO4FNeNt5xdD4yilDW5oP8vu7yNln%2FO%2BuTnXfp98utXEpy7RS9PMJmXD1wOli0lApTM0wiJTsCZM3ieYoZuMhiKs8%2Fc5dw2ZbOkPK0PqhznE6IMLSqmcpBfEJkhRpe8iaRMiVdJGIn08wZ94Je2aRV5iTMsPR6ve96Awj%2BUuLwAI7Afo%2FwRsVCMzuIYZASnbDUIb8B%2F%2BLCGxa%2FHmw6FpWN7BqPJ5utGoDfj%2FwHTHVSjyebrRqA3E0dy1HWjyeZ7%2BojVq4HhaqBczX%2BcAZmzBKdouJ7gAuMJSdmQJISu8Hf437Hw6CCmMMKods7tD%2Bxev3JuhCnvCJOUn08JFawaTHCSVK4BoDviznMGOaPkEVXOTFZ%2F%2BJkI5tPVrBDDEezGXDSu4ANKrkmOy%2B4fCGNkVmnQT3AsTjAiJg4sj0I%2BKkTrM0k8YSmHwJbHJePELWGeFXBM8EKMY8D1JRMnZ4tYKHEHPuduh6KczGmILkMxngE%2FLD7VW3GFfeQjuodpdA%2Bz7J4%2FNYIznMbHmdGeA2pT2vG1Ke0H%2BoyWtqNPaFub0LfogRv6WabNbP6IrO6YOiVSkiKFP6VJc67KgRmOInEbo6ZuVNc6khPcuq6u9bLiha5BV522ZNXRvHBNUYRXMzM%2F%2BSq0hkfCBTwNrp4BLrctuDwNrv715f%2BYrnbHqzvgxHTt7o8C8GwVTFbRL00jPIv5XRPMZWYcJphLLWXiI5llcw435%2Ft4BBl8gDm6B3aw4L%2BdjOvvMYhcx3GNUAXIwABk0BaQvgakfPIGbH5nLO0q2BpE4k1JGuwnqRY3VNCtR64jE96S42p4YiI6%2FD2nSDxRjFJEIR%2F9eIwTlHfyp2NFFkqyALoGlXANoUVbDujtd0AtV6hSWwvoTMq9ziKtJrOhCDOV4NYZBKMxMESMcZjZnUjKkHME%2F7iW4h%2BD%2BBiTOastB8llZJeHUBr1RelAIJvAPMdh3VN1GeHo0OUvcdDpuY403K0MbiCPR4tq89GyenSNKOZPJzxYGBeYiQ7PrY7l%2BqWh7NDulcebDsXBsnKgdRfFSGYOIt0hMUlhcrGxbp%2BJRfKwX3AYpDFi%2B%2BeFGMpO3lR44Rl4IW0UJZDhp3qNxsSV8g7XQtiqwUWdlmuRll0Uz11eVa2pqB35SkdA6agARutoRd31Y7%2BCzQ1qEy9kc8k9q0Y7byfpcv6UTL%2FHyswFf29UXmXZH2m0TM4v3OkounIGf98NRsw9B25DmrnvimaOp7CjdyDNVBnVsoy2aaZnzM1otoUZTbTUqyop2CejkrVrpt5ViWpk7eGi1%2F2QbOweiYwAnJiMeibcNhnri7q3j4y71nTwAl1tc%2BFuqqjgXXFYJTHwDiSxo5BYCzjbJrFeTvgx55RBOTduzYdPXQSTm3mnqoEBU3rVTUSNgOeb3Vh86GM6SfgUty27Y8mz%2FG7rBhqq%2B2pmPGXqhgF6mOipVARRMAnfX13C6QV1ehsKE74hLz5GYcIcwe133BjmbFXS%2FJwu0wrOb1fvNHrMFPIpHiu2iRLMPqvP1htbp3KSaftecdI1yVlM0c2Pq8%2FqJWXjy%2FZ1LQy8t9TC7V6L8JP0jAgCeKPNnljFfZVmJ48RnJ4Cr6HE11aQYIZXL4J%2FIylmhGK5oXJCuGyZrci98FPDJZedXRryhcIJTOFnFRDupLrPDArSVjT1dHGZPXxdPg6DQfbP94UDfv512eSNpAOrfrX6icxVt2Snh6bHDbNaJeU8Wqlmh2icKq3V6nuH1qNdteLYXj3aSEw9aCyXsR9zPqfZ8hjyq81bAzOar1b%2B28mvETH9LRhDLHBFQrF7at3wRUxss7YWCbwKW%2FUNI9OrmyZsW5PJBi%2B3HrrV9zLJM%2B7kvqkO9nQd3E7Hk23LKbtprlqUayqDXSWXdtQyYcsyeGiFusH63PPrFWTf371Im%2FaDP8LC%2FSEI6wRHWrc9RyFse%2BVoI4p6NTqmCLJ7tBDvpEDzK5nvM9J%2F1RLmbvND9dsH9nHWMH64%2BfJH4cjNN2ici%2F8A)
