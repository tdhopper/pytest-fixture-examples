import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pytest-fixture-examples",
    version="1.0.0",
    author="Tim Hopper",
    description=(
        "An demonstration of how to create, document, and publish "
        "to the cheese shop a5 pypi.org."
    ),
    license="Public Domain",
    packages=["lib"],
    install_requires=["pytest", "pandas", "black", "pylint", "pytest-sugar"],
    long_description=read("README.md"),
)
