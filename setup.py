from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
   name='mlproject',  #name of the package
   version='0.0.1',
   description='An end to end ML project',
   author='Noel',
   author_email='dalmasnoel@gmail.com',
   packages=find_packages(), #packages to include
   install_requires=get_requirements('requirements.txt'), #dependencies
)