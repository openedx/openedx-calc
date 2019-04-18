from __future__ import absolute_import
from setuptools import setup

setup(
    name="calc",
    version='0.4',
    packages=["calc"],
    install_requires=[
        "pyparsing==2.2.0",
        "numpy",
        "scipy",
    ],
    test_suite='calc.tests',
    tests_require=[
        'coverage',
    ],
)
