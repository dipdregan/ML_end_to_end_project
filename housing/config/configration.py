from housing.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,\
                                        DataTransformationConfig  
# ,DataTransformationConfig,ModelTrainerConfig,ModelPusherConfig,ModelEvaluationConfig
from housing.exception import HousingException
from housing.logger import logging
from housing.utils.util import read_yaml_file
from housing.constant import *

import os,sys


class Configration:
    def __init__(self, config_file_path:str = CONFIG_FILE_PATH,
                 current_time_stamp:str = CURRENT_TIME_STAMP) -> None:     
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp

        except Exception as e:
            raise e
        
    def get_data_ingestion_config(self)->DataIngestionConfig:
        """
        retrun : entity (DataIngetionConfig)
        """
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            data_ingestion_artifact_dir = os.path.join(artifact_dir,
                                           DATA_INGESTION_ARTIFACT_DIR,
                                           self.time_stamp
                                           )
            
            dataset_download_url=data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]

            tgz_download_dir=os.path.join(data_ingestion_artifact_dir,
                                          data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,
                                      data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            
            ingested_dir=os.path.join(data_ingestion_artifact_dir,
                                    data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            
            ingested_train_data=os.path.join(ingested_dir,data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            
            ingested_test_data=os.path.join(ingested_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])

            data_ingestion = DataIngestionConfig(dataset_download_url=dataset_download_url,
                                raw_data_dir=raw_data_dir,
                                tgz_download_dir=tgz_download_dir,
                                ingested_dir=ingested_dir,
                                ingested_train_dir=ingested_train_data,
                                ingested_test_dir=ingested_test_data)
            return data_ingestion

        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_validation_config(self)->DataValidationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_validation_artifact_dir = os.path.join(
                                                        artifact_dir,
                                                        DATA_VALIDATION_ARTIFACT_DIR_NAME,
                                                        self.time_stamp
                                                    )
            data_validation_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            schema_file_path = os.path.join(ROOT_DIR,
                                            data_validation_info[DATA_VALIDATION_SCHEMA_DIR_KEY],
                                            data_validation_info[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]
                                            )

            report_file_path = os.path.join(data_validation_artifact_dir,
                                            data_validation_info[DATA_VALIDATION_REPORT_FILE_NAME_KEY])
            
            report_page_file_path = os.path.join(data_validation_artifact_dir,
                                                 data_validation_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY])

            data_validation_config = DataValidationConfig(
                schema_file_path=schema_file_path,
                report_file_path=report_file_path,
                report_page_file_path=report_page_file_path
            )
            return data_validation_config
        
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_transformation_config(self)->DataTransformationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_transforamation_artifact_dir = os.path.join(
                artifact_dir,
                DATA_TRANSFORAMATION_ARTIFACT_DIR,
                self.time_stamp
            )
            
            data_transforamation_config_info=self.config_info[DATA_TRANSFORAMATION_CONFIG_KEY]
            add_bedroom_per_room = data_transforamation_config_info[DATA_TRANSFORAMATION_ADD_BEDROOM_PER_ROOM_KEY]

            preprocessed_object_file_path = os.path.join(
                data_transforamation_artifact_dir,
                data_transforamation_config_info[DATA_TRANSFORAMATION_PREPROCESSING_DIR_KEY],
                data_transforamation_config_info[DATA_TRANSFORAMATION_PREPROCESSED_FILE_NAME_KEY],
            )
            
            transformed_train_dir = os.path.join(
                data_transforamation_artifact_dir,
                data_transforamation_config_info[DATA_TRANSFORAMATION_DIR_NAME_KEY],
                data_transforamation_config_info[DATA_TRANSFORAMATION_TRAIN_DIR_NAME_KEY]
            )

            transformed_test_dir = os.path.join(
                data_transforamation_artifact_dir,
                data_transforamation_config_info[DATA_TRANSFORAMATION_DIR_NAME_KEY],
                data_transforamation_config_info[DATA_TRANSFORAMATION_TEST_DIR_NAME_KEY]
            )

            data_transformation_config = DataTransformationConfig(
                                                add_bedroom_per_room=add_bedroom_per_room,
                                                preprocessed_object_file_path=preprocessed_object_file_path,
                                                transformed_train_dir=transformed_train_dir,
                                                transformed_test_dir=transformed_test_dir
                                                )
            logging.info(f"Data transformation config : {data_transformation_config}")
            return data_transformation_config

        except Exception as e:
            raise HousingException(e,sys) from e

    # def get_model_trainer_config(self)->ModelTrainerConfig:
    #     pass

    # def get_model_evaluation_config(self)->ModelEvaluationConfig:
    #     pass

    # def get_model_pusher_config(self)->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]

            artifact_dir = os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipeline Config : {training_pipeline_config}")

            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e