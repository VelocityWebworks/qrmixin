#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='qrmixin',
    version='0.1',
    description="A collection of fabric utils",
    author="Danemco, LLC",
    author_email='dev@velocitywebworks.com',
    url='https://git.velocitywebworks.com/lib/danemco-fabric.git',
    packages=find_packages(),
    install_requires=['fabric>=1.7.0', 'requests', 'python-gitlab'],
)
