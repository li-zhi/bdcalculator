#!/usr/bin/env python

# this script allows us to publish bdcalculator in PyPi and the use it using 'pip install bdcalculator'
# run 'python setup.py sdist bdist_wheel' to create the distribution files within bdcalculator

from setuptools import setup


setup(
    name="bdcalculator",
    setup_requires=["setupmeta"],
    versioning="dev",
    author="Zhi Li",
    author_email="zli@netflix.com",
    include_package_data=True,
    url="https://github.com/li-zhi/bdcalculator",
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT Software License",
        "Operating System :: MacOS",
        'Operating System :: Unix',
    ]
)
