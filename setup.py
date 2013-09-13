#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mnowotka'

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='chembl_ikey',
    version='0.0.1',
    author='Michal Nowotka',
    author_email='mnowotka@ebi.ac.uk',
    description='Pure python implementation of InChiKey generation algorithm based on the original C code',
    url='https://www.ebi.ac.uk/chembl/',
    license='CC BY-SA 3.0',
    packages=['chembl_ikey'],
    long_description=open('README.rst').read(),
    include_package_data=False,
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Intended Audience :: Developers',
                 'License :: Creative Commons :: Attribution-ShareAlike 3.0 Unported',
                 'Topic :: Scientific/Engineering :: Chemistry'],
    zip_safe=False,
)