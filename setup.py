from setuptools import find_packages,setup

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) ->list[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='RegressionProject',
    version='0.0.1',
    author='Akash',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)