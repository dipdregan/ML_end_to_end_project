from housing.pipeline.pipeline import Pipeline
from housing.config.configration import Configration
from housing.exception import HousingException
import sys
from housing.components.data_transformation import DataTransformation

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_validation_config = Configration().get_data_transformation_config()
        # print(data_validation_config)

        # schema_file_path = r'F:\Machine_Learnig _End_to_end_project\ML_end_to_end_project_by_Avnish\config\schema.yaml'
        # file_path = r'F:\Machine_Learnig _End_to_end_project\ML_end_to_end_project_by_Avnish\housing\artifact\data_ingestion\2023-06-23_08-15-20\ingested_data\train\housing.csv'

        # df = DataTransformation.load_data(file_path=file_path,schema_file_path= schema_file_path)
        # print(df.dtypes)
        # print(df.columns)
    except Exception as e:
        raise HousingException(e,sys) from e




if __name__ =="__main__":
    main()