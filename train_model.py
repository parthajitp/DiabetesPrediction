from sklearn.model_selection import train_test_split
import pandas as pd
from model_training import clustering
from model_finder import model_finder
import pickle
import os
import shutil

class ModelTrainClass:
    def model_training_func(self):
        try:
            data = pd.read_csv('input_data/diabetes_data_train.csv')
            X, Y = data.drop('class', axis=1), data['class']
            X = pd.get_dummies(X)
            kmeans= clustering.KMeansClustering() # object initialization.
            number_of_clusters=kmeans.elbow_plot(X)  #  using the elbow plot to find the number of optimum clusters

            # Divide the data into clusters
            X=kmeans.create_clusters(X,number_of_clusters)

            #create a new column in the dataset consisting of the corresponding cluster assignments.
            X['Labels']=Y

            X.to_csv("Training_logs/X.csv", header=True, mode='a+')

            # getting the unique clusters from our dataset
            list_of_clusters=X['Cluster'].unique()

            for i in list_of_clusters:
                cluster_data = X[X['Cluster'] == i]  # filter the data for one cluster

                # Prepare the feature and Label columns
                cluster_features = cluster_data.drop(['Labels', 'Cluster'], axis=1)
                cluster_label = cluster_data['Labels']

                # splitting the data into training and test set for each cluster one by one
                x_train, x_test, y_train, y_test = train_test_split(cluster_features, cluster_label, test_size=1 / 3,
                                                                    random_state=355)

                model_finder_obj = model_finder()  # object initialization

                # getting the best model for each of the clusters
                best_model_name, best_model = model_finder_obj.get_best_model(x_train, y_train, x_test, y_test)

                path = os.path.join('models/', best_model_name + str(i))  #
                if os.path.isdir(path):  # remove previously existing models for each clusters
                    shutil.rmtree(path)
                    os.makedirs(path)
                else:
                    os.makedirs(path)  #
                with open(path + '/' + best_model_name + str(i) + '.sav', 'wb') as f:
                    pickle.dump(best_model, f)  # save the model to file

            return "Success"
        except Exception as e:
            raise Exception()