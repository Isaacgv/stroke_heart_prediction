from data_processing import pipeline_test
import pickle


def make_prediction(X):
    X = pipeline_test(X)
    file = "../models/classifier.pickle"
    classifier = pickle.load(open(file, "rb"))
    return classifier.predict(X)
