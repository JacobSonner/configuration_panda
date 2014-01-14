from setuptools import setup, find_packages

import configuration_panda

requirements = open('requirements.txt')

setup(
    name="ConfigurationPanda",
    packages=find_packages(),
    version=configuration_panda.__version__,
    author="Mike Dunn",
    author_email="mike@eikonomega.com",

    install_requires=requirements,
    include_package_data=True
)

