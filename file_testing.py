from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
import os,sys
from housing.logger import logging
from housing.config.configration import Configuartion

def main():
    try: 
        #<<<<this is use for data ingestion>>>>
        #pipeline = Pipeline()
        #pipeline.run_pipeline()

        data_validation_config = Configuartion().get_data_validation_config()
        print(data_validation_config)
    except Exception as e:
        logging.error(f"[{e}]")
        print(e)

if __name__ == "__main__":
    main()      