from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import  DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import os,sys

class DataValidation:

    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact) -> None:
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def is_train_test_file_exits(self):
        try:
            logging.info(f"{'=='*10}Checking if train and test file are available{'=='*10}")

            is_train_file_exits = False
            is_test_file_exits = False
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exits = os.path.exists(train_file_path)
            is_test_file_exits = os.path.exists(test_file_path)

            is_available =  is_train_file_exits and is_test_file_exits
            logging.info(f"Is train and test file exits ?----> {is_available}")
            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path

                message = f"Training file : {training_file} or Testing file : {testing_file} "\
                            "is not present"
                logging.info(message)
                raise Exception(is_available)

            return is_available
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def validate_dataset_schema():
        try:
            validation_status = False
            
            validation_status = True
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def initiate_data_validation(self):
        try:
            
            self.is_train_test_file_exits()
            self.validate_dataset_schema()

        except Exception as e:
            raise HousingException(e,sys) from e
        
