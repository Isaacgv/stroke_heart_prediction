<<<<<<< HEAD
from data_processing import pipeline
=======
from data_processing import pipeline_test
>>>>>>> 4b4cd442ff939aa35e173927097270e09b80f9e9
import pickle


def make_prediction(X):
    X = pipeline(X)
    file = "../models/classifier.pickle"
    classifier = pickle.load(open(file, "rb"))
    return classifier.predict(X)
