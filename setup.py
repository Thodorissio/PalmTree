#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="pre-trained-palmtree",
    version="0.1",
    description="PreTrained Palmtree",
    packages=setuptools.find_packages(),
    install_requires=[
        "torch>=10.1",
        "cuda>=10.1",
    ],
)
