from collections import namedtuple

"""
Here I am specifying the structure of the configuration of all the steps 
and these strecture called the enetity
"""

DataIngestionnConfig = namedtuple('DataIngestionConfig',['dataset_download_url','tgz_download_dir',
                                                         'raw_data_dir','ingested_train_dir','ingested_test_dir'])

# scheam file path to validate the data 
DataValidationConfig = namedtuple('DataValidationConfig',['schema_file_path',
                                                          'report_file_path',
                                                          'report_page_file_path'])

#data transformation
DataTransformationConfig = namedtuple('DataTransformationConfig', ['add_bedroom_per_room',
                                                                  'transform_train_dir',
                                                                  'transform_test_dir',
                                                                  'preprocessed_object_file_path'])

ModelTrianConfig = namedtuple('ModelTrianConfig',['train_model_file_path','base_accuracy'])

ModelEvaluationConfig = namedtuple('ModelEvaluationConfig',['model_evaluation_file_path','time_stamp'])

ModelPusherConfig = namedtuple('ModelPusherConfig',['export_dir_path'])

TrainingPipelineConfig = namedtuple('TrainingPipelineConfig',['artifact_dir'])