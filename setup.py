# created with help from https://www.youtube.com/watch?v=Rv6UFGNmNZg&ab_channel=KrishNaik
from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> list[str]:
    """
    Returns the list of requirements sepcified per line in file_path
    """
    requirements = []
    with open(file_path) as file_object:
        lines_raw = file_object.readlines()
        requirements = [l.strip() for l in lines_raw]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='ml_project',
version='0.0.1',
author='Jemima',
author_email='jemima.goodall@gmail.com',
packages=find_packages(),
install_requirements=get_requirements("requirements.txt")
)