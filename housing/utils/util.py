import yaml
from housing.exception import HousingException
from housing.logger import logging
import sys, os
import pprint

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
        
        
