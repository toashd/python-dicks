#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="python-dicks",
      version="1.0.0",
      description='A Python client for the Dicks API',
      license="MIT",
      install_requires=["simplejson","requests"],
      author="Tobias Schmid",
      author_email="toashd@gmail.com",
      url="http://github.com/toashd/python-dicks",
      packages = find_packages(),
      keywords= "dicks, dicks as a service",
      zip_safe = True)

