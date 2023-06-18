from housing.pipeline.pipeline import Pipeline
from housing.config.configration import Configration

def main():
    pipeline = Pipeline()
    pipeline.run_pipeline()
    # data_validation_config = Configration().get_data_validation_config()
    # print(data_validation_config)


if __name__ =="__main__":
    main()