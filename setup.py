#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

version = "1.0.0"

# python setup.py tag
if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

# python setup.py publish
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

setup(name="python-dicks",
      version=version,
      description='A Python client for the Dicks API',
      license="MIT",
      install_requires=["simplejson","requests"],
      author="Tobias Schmid",
      author_email="toashd@gmail.com",
      url="http://github.com/toashd/python-dicks",
      packages = find_packages(),
      keywords= "dicks, dicks as a service",
      zip_safe = True)

