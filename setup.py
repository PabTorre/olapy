# -*- coding: utf-8 -*-
"""
Setupscript for olapy python 

"""

from distutils.core import setup
setup(name='olapy',
	version='0.0.1',
	description='generic OLAP Cube aplication',
	long_description = open('README.txt').read(),
	##scripts = ['bin/examples.py'],
	license = 'LICENSE.txt',
	author='Pablo Torre',
	url = 'www.fractalsoft.biz',
	author_email = 'xctico@gmail.com',
	packages=['olapy'],
	requires=[
	'pandas (>= 0.13.1)', 
	'numpy (>= 1.8.1)', 
	'psycopg2 (>= 2.5.2)'])
