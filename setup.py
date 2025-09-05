from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements'''

    requiements = []
    with open(file_path) as file_obj:
        requiements = file_obj.readlines()
        requiements = [req.replace("\n", "") for req in requiements]

        if HYPEN_E_DOT in requiements:
            requiements.remove(HYPEN_E_DOT)
    return requiements


setup(
    name="mlnewproject",
    version="0.0.1",
    author="Madhav",
    author_email="madhav@example.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
