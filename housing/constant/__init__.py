from datetime import datetime 
import os

ROOT_DIR = os.getcwd()
#ROOT_DIR = os.getcwd() # To get the current working dir
CONFIG_DIR ='config'
CONFIG_FILE_NAME = 'config.yaml'


CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"


# Training pipeline related variable

TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_ARTIFACT_DIR = 'artifact_dir'
TRAINING_PIPELINE_NAME_KEY  = 'pipeline_name'

## Data ingestion realted variable 


DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR = 'data_ingestion'# thsi is a folder name that's why i am not giving inside the yaml file
DATA_INGESTION_DOWNLOAD_URL_KEY = 'dataset_download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = 'tgz_download_dir'
DATA_INGESTION_INGESTED_DIR_NAME_KEY = 'ingested_dir'
DATA_INGESTION_TRAIN_DIR_KEY = 'ingested_train_data'
DATA_INGESTION_TEST_DIR_KEY = 'ingested_test_data'