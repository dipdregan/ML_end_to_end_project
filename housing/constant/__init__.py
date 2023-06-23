import os
from datetime import datetime

ROOT_DIR = os.getcwd() # to get current working directory

CONFIG_DIR = "config"
CONFIG_FILE_NAME = 'config.yaml'

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

SCHEMA_FILE_NAME = 'schema.yaml'
SCHEMA_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,SCHEMA_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Training pipeline related variable

# training_pipeline_config:
#   pipeline_name : housing
#   artifact_dir : artifact


TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'


# data ingetion related variable 
# data_ingestion_config :
#   dataset_download_url : https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz
#   raw_data_dir : raw_data
#   tgz_download_dir : tgz_data
#   ingested_dir : ingested_data
#   ingested_train_data : train
#   ingested_test_data : test

DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR = 'data_ingestion'
DATA_INGESTION_DOWNLOAD_URL_KEY = 'dataset_download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = 'tgz_download_dir'
DATA_INGESTION_INGESTED_DIR_NAME_KEY = 'ingested_dir'
DATA_INGESTION_TRAIN_DIR_KEY = 'ingested_train_data'
DATA_INGESTION_TEST_DIR_KEY = 'ingested_test_data'

# ## Data Validation Related variable 

# data_validation_config:
#   schema_dir : config
#   schema_file_name : schema.yaml
#   report_file_name : report.json
#   report_page_file_name : report.html

DATA_VALIDATION_CONFIG_KEY = 'data_validation_config'
DATA_VALIDATION_SCHEMA_DIR_KEY = 'schema_dir'
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY ='schema_file_name'
DATA_VALIDATION_ARTIFACT_DIR_NAME ='data_validation'
DATA_VALIDATION_REPORT_FILE_NAME_KEY = 'report_file_name'
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = 'report_page_file_name'

# Data Transformation related variable

# data_transformation_config:
#   add_bedroom_per_room : true
#   transformed_dir : transformed_data
#   transformed_train_dir : train
#   transformed_test_dir : test
#   preprocessing_dir : preprocessed
#   preprocessed_object_file_name : preprocessed.pkl

DATA_TRANSFORAMATION_ARTIFACT_DIR = 'data_transforamation'
DATA_TRANSFORAMATION_CONFIG_KEY = 'data_transformation_config'
DATA_TRANSFORAMATION_ADD_BEDROOM_PER_ROOM_KEY = 'add_bedroom_per_room'
DATA_TRANSFORAMATION_DIR_NAME_KEY = 'transformed_dir'
DATA_TRANSFORAMATION_TRAIN_DIR_NAME_KEY = 'transformed_train_dir'
DATA_TRANSFORAMATION_TEST_DIR_NAME_KEY = 'transformed_test_dir'
DATA_TRANSFORAMATION_PREPROCESSING_DIR_KEY = 'preprocessing_dir'
DATA_TRANSFORAMATION_PREPROCESSED_FILE_NAME_KEY = 'preprocessed_object_file_name'


COLUMN_TOTAL_ROOMS = 'total_rooms'
COLUMN_POPULATION = 'population'
COLUMN_HOUSEHOLDS = 'households'
COLUMN_TOTAL_BEDROOM = 'total_bedrooms'
DATASET_SCHEMA_COLUMNS_KEY = 'columns'

NUMERICAL_COLUMN_KEY = 'numerical_columns'
CATEGORICAL_COLUMN_KEY = 'categorical_columns'

TARGET_COLUMN_KEY = 'target_column'