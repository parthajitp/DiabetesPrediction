import pickle
import os
import shutil

class file_operation:

    def __init__(self):
        self.model_directory='models/'

    def load_model(self, filename):
        try:
            with open(self.model_directory + filename + '/' + filename + '.sav', 'rb') as f:

                return pickle.load(f)
        except Exception as e:
            raise Exception()

    def find_correct_model(self, cluster_num):
        try:
            self.cluster_num = cluster_num
            self.model_directory = 'models/'
            self.list_model_files = []
            self.list_of_files = os.listdir(self.model_directory)
            for self.file in self.list_of_files:
                if self.file.find(str(self.cluster_num)) != -1:
                    self.model_name = self.file
                else:
                    continue
            self.model_name = self.model_name.split('.')[0]
            return self.model_name
        except Exception as e:
            raise Exception()
