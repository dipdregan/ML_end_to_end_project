from setuptools import setup
from typing import List


# Declaring variables for setup functions
Project_name ='housing-predictor'
VERSION = '0.0.1'
Author = 'Dipendra_Pratap'
Email = 'dipendrapratap55@gmail.com'
DES = 'This is my first end to end project'
PACKEGES = ['housing']
REQUIREMENT_FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    """Description : this fuction going to return list of requirement
    mention in requirement.txt file

    Returns:
        List[str]: this fuction going to return a list 
        which contain name of libraries mentained requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name=Project_name,
    version=VERSION,
    author=Author,
    author_email=Email,
    description=DES,
    packages=PACKEGES,
    install_requires = get_requirements_list()
)
