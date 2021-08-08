import pandas as pd
import pickle
import os
import shutil
from file_ops import file_operation
class prediction:
    def __init__(self):
        self.saved_model_path_kmeans = 'models/KMeansModel'

    def prediction_Model(self):

        try:
            file_ops_obj = file_operation()
            data = pd.read_csv('input_data/diabetes_data_test.csv')
            data = data.drop('class', axis=1)
            data = pd.get_dummies(data)
            kmeans = file_ops_obj.load_model('KMeansModel')
            cluster = kmeans.predict(data)
            data['clusters'] = cluster
            clusters = data['clusters'].unique()
            for i in clusters:
                cluster_data = data[data['clusters'] == i]
                cluster_data = cluster_data.drop(['clusters'], axis=1)
                model_name = file_ops_obj.find_correct_model(i)
                model = file_ops_obj.load_model(model_name)
                result = list(model.predict(cluster_data))
                result = pd.DataFrame(list(zip(result)), columns=['Prediction'])
                result.to_csv("Prediction_Output_File/Predictions.csv", header=True, mode='a+')
            return "success"

        except Exception as e:
            raise Exception()
