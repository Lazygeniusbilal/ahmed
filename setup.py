from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirments(file_path:str) ->List[str]:
    '''
    this fuction will return list of requirements

    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:

            requirements.remove(HYPEN_E_DOT)
    return requirements        






setup(
      name = 'ML_Project',
      version = '0.0.1',
      author = 'Bilal',
      author_email = 'bilal.ahmed38980@gmail.com'
      packages = find_packages()
      install_requires = get_requirments('requirements.txt')



)