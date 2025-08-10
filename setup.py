from setuptools import setup, find_packages
from typing import List

def read_requirements() -> List[str]:
    """Read requirements from a file and return a list of packages."""
    requirement_list: list[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Proceeding without it.")

    # The return statement must be outside the try-except block
    return requirement_list

setup(
    name='network_security',
    version='0.0.1',
    author='westobaba',
    author_email='westobaba@gmail.com'
    packages=find_packages(),
    install_requires=read_requirements(),
    description='A package for network security analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
# Note: The 'numpy' package is added to the requirements list in the requirements.txt file.
# The '-e .' line is ignored as per the instructions.