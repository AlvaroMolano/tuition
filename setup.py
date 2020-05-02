# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in tuition/__init__.py
from tuition import __version__ as version

setup(
	name='tuition',
	version=version,
	description='Add flavour and utilities to education module',
	author='AlvaroMolano',
	author_email='al.j.molano@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
