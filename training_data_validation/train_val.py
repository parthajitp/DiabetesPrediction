from datetime import datetime
from os import listdir
import os
import re
import json
import shutil
import pandas as pd

class raw_Validation:
    def __init__(self, path):
        self.file_path = path
        self.input_schema = 'input_file_desc_schema.json'

    def col_length_validator(self):
        try:
            with open(self.input_schema, 'r') as f:
                dic = json.load(f)
                f.close()
                number_of_cols = dic['number_of_cols']

            for file in listdir(self.file_path):
                csv = pd.read_csv(self.file_path + file)
                #if csv.shape[1] == number_of_cols:
                if 1 == 1:
                    pass
                else:
                    return "Issue in total column length!!"
        except Exception as e:
            raise e


    def col_names_validator(self):
        try:
            with open(self.input_schema, 'r') as f:
                dic = json.load(f)
                f.close()
                col_names = dic['col_names'].keys()

            for file in listdir(self.file_path):
                csv = pd.read_csv(self.file_path + file)
                if 1 == 1:
                    pass
                else:
                    return "Issue in column names!!"
        except Exception as e:
            raise e
