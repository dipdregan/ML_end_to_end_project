import yaml
from housing.exception import HousingException
from housing.logger import logging
import sys, os
import pprint

import numpy as np
import dill
import pandas as pd
from housing.constant import *


def read_yaml_file(file_path:str) ->dict:
    
        """
        This fuction use for reading a yaml file and return the  content as dictionary
        file_path :str

        """
        try:
            with open(file_path,'rb') as yaml_file:
                yaml_file = yaml.safe_load(yaml_file)
                logging.info(f"Sucessfully read yaml files")
                my_complex_dict = pprint.pformat(yaml_file)
                logging.info(f"My complex dict:\n{my_complex_dict}")
                return yaml_file
            
            
        except Exception as e:
            logging.info(f"Error Occured in {HousingException(e,sys)}")
            raise HousingException(e,sys) from e
        
   
def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
    try:
        dataset_schema = read_yaml_file(schema_file_path)

        schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
        dataframe = pd.read_csv(file_path)

        error_messagae = ""

        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                    error_messagae = f"{error_messagae}\n Column: [{column}] is not in the schema."
        if len(error_messagae) > 0:
                raise Exception(error_messagae)
        return dataframe

    except Exception as e:
        raise HousingException(e,sys) from e
        
        
def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok= True)

        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)

    except Exception as e:
        raise HousingException(e,sys) from e

def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path,'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e
        
def save_object(file_path:str,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e
        
def load_object(file_path:str):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise HousingException(e,sys) from e
        

