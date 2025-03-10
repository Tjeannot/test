from setuptools import setup, find_packages

def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="ml_toolkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    description="A simple machine learning toolkit for classification and regression",
) 