from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.Data_validation import DataValidation
from textSummarizer.logging import logger

class DataValidationTrainingPipepline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()