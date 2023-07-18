from setuptools import find_packages,setup
from typing import List

HYPHENEDOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function returns the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHENEDOT in requirements:
            requirements.remove(HYPHENEDOT)

    return requirements
setup(
    name='Concrete strength',
    version='0.0.1',
    author='Kamalashree',
    author_email='kamalashree.sudhakar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)