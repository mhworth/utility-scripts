"""
This script assumes that you installed sage already and you're using that python distribution in your PATH

Well, it doesn't have to be sage actually, it could be any python distribution, but still, the idea is to do it with sage

"""
import os

PYTHON_PACKAGES = """tables
configobj
pexpect
xlrd
xlwt
sympy
elementtree
pil"""

for package in PYTHON_PACKAGES.split("\n"):
  os.system("easy_install %s" % package)

SAGE_PACKAGES = """wxPython-2.8.7.1"""

for package in SAGE_PACKAGES.split("\n"):
  os.system("sage -i %s" % package)
