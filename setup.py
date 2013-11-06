from setuptools import setup, find_packages

import configuration_panda

setup(
    name="ConfigurationPanda",
    packages=find_packages(),
    version=configuration_panda.__version__,
    author="Mike Dunn",
    author_email="mike@eikonomega.com"
)

