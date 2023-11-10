from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as file:
	content = file.readlines()
requirements = [x.strip() for x in content]

setup(name='titanic',
	description="KNN model, APP and API for the titanic problem (kaggle).",
	packages=find_packages(),
	install_requires=requirements)