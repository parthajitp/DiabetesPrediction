from training_data_validation.train_val import raw_Validation


class train_Validation_Master():
    def __init__(self, path):
        self.path = path
        self.file_object = open("Training_logs/Training_master_log.txt", 'a+')
        self.raw_data = raw_Validation(self.path)

    def train_validation(self):
        col_name_validation = self.raw_data.col_names_validator()
        col_length_validation = self.raw_data.col_length_validator()

        if bool(col_name_validation) or bool(col_length_validation):
            return "Issue with Training file"
        else:
            pass
