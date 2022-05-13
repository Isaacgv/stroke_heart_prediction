#!/bin/bash

streamlit run web_interface.py

cd /home/it/stroke_heart_prediction/stroke_api
uvicorn  main:app --host 0.0.0.0 --port 8005