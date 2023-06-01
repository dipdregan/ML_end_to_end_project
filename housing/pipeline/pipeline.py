from housing.config.configration import Configuartion
from housing.logger import logging
from housing.exception import HousingException

from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionnConfig
from housing.components.data_ingestion import DataIngestion

import os,sys

class Pipeline:

    def __init__(self, config:Configuartion = Configuartion()) -> None:
        try:
            self.config =config

        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())

            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
        

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def run_pipeline(self):
        try:
            #data ingestion
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e
        
    