from stroke_prediction.data_processing import (pipeline_train,
                                               build_model,
                                               evaluate_model)


def make_model_train(df):
    xtrain, ytrain, xtest, ytest = pipeline_train(df)
    build_model(xtrain, ytrain)
    return evaluate_model(xtest, ytest)
