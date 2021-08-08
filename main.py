# Import Libraries


from flask import Flask, request, render_template, Response
import os
from wsgiref import simple_server
from training_master import train_Validation_Master
from train_model import ModelTrainClass
from predict_model import prediction
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hi():
    return Response("Hi!! My name is Parthajit. We are going to predict the early stages of diabetes using the data from the following website -"
                    "https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.")


@app.route("/train", methods=['GET'])
def trainModel():
    train_path_default = "input_data/"
    train_obj = train_Validation_Master(train_path_default)
    train_result = train_obj.train_validation()
    #if bool(train_result):
    #    return Response("Training Validation Complete")
    #else:
    #    return Response(train_result)
    train_model_obj = ModelTrainClass()
    train_model_obj.model_training_func()
    return Response("Training  Complete")

@app.route("/predict", methods=['GET'])
def predict():
    pred_obj = prediction()
    pred_model_obj = pred_obj.prediction_Model()
    return Response("Prediction  Complete")


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
