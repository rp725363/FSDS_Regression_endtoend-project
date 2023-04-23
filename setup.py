from setuptools import find_packages,setup
from typing import List

hyphen="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hyphen in requirements:
            requirements.remove(hyphen)

    return requirements


setup(
    name='RegressorProject',
    version='0.0.1',
    author='Krissh',
    author_email='krish.naik@ineuron.ai',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)