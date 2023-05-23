from setuptools import setup,find_packages
from typing import List


# Declaring variables for setup functions
Project_name ='housing-predictor'
VERSION = '0.0.0'
Author = 'Dipendra_Pratap'
Email = 'dipendrapratap55@gmail.com'
DES = 'This is my first end to end project'
PACKEGES = find_packages()


def get_requirements_list(filepath:str)->List[str]:
    """Description : this fuction going to return list of requirement
    mention in requirement.txt file

    Returns:
        List[str]: this fuction going to return a list 
        which contain name of libraries mentained requirements.txt file
    """
    requirement = []
    with open(filepath) as requirement_file:
        return requirement_file.readlines().remove('-e .')


setup(
    name=Project_name,
    version=VERSION,
    author=Author,
    author_email=Email,
    description=DES,
    packages=PACKEGES,
    install_requires = get_requirements_list('requirements.txt')
)
