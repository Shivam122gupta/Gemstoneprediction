from setuptools import find_packages ,setup
from typing import List



Hypen_E_dot = '-e .'
def get_requirements(file_path:str)->List[str]:   #this function will return the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        [req.replace('\n'," ")for req in requirements]
        
        if Hypen_E_dot in requirements:
            requirements.remove(Hypen_E_dot)
    return requirements     



setup(
name='mlproject',
version='0.0.1',
author='Shivam',
author_email='22shivamgupta05@gmail.com',
packages = find_packages(),
install_requires=get_requirements('requirements.txt')
)