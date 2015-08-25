#!/bin/bash

###  Create the distribution

git log > CHANGES.txt
python setup.py sdist

sudo pip install ../olapy/
####   Upload the distribution to open repository -- for later use. 

# python setup.py register
# python setup.py sdist upload
