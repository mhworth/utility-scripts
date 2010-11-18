#!/usr/bin/python

"""
This script downloads and installs all of the necessary analysis packages for python data analysis, based on sage.
"""

SAGE_VERSION="4.4.4"
SAGE_BASE_URL="http://mirror.switch.ch/mirror/sagemath/src/"
SAGE_FILENAME="sage-4.4.4.tar"


import os,sys,re

# Check our os
if not os.name=="posix":
  print "This script will only work on a linux machine!"
  sys.exit(1)

# List of all python packages that can be installed with EasyInstall
PYTHON_PACKAGES = """tables
configobj
pexpect
xlrd
xlwt
sympy
elementtree
pil"""
PYTHON_PACKAGES = PYTHON_PACKAGES.split("\n")

# List of all packages that need to be installed if we're on a debian variant
DEBIAN_PACKAGES = """libhdf5-openmpi-dev"""
DEBIAN_PACKAGES = DEBIAN_PACKAGES.split("\n")

# List of all packages that need to be installed if we're on a RHEL variant
RHEL_PACKAGES = """hdf5-devel"""
RHEL_PACKAGES = RHEL_PACKAGES.split("\n")



