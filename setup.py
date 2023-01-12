from setuptools import setup, find_packages

setup(
    name="pre-trained-palmtree",
    version="0.1",
    description="pre-trained-palmtree",
    packages=find_packages(),
    install_requires=[
        "torch>=1.10+cu>=110",
    ],
)
