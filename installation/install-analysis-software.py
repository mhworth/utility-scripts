#!/usr/bin/python

"""
This script downloads and installs all of the necessary analysis packages for python data analysis, based on sage and root.
"""

ROOT_VERSION="5.27.04"
ROOT_FILENAME="root_v%s.source.tar.gz"%(ROOT_VERSION,)
ROOT_BASE_URL="ftp://root.cern.ch/root/"

SAGE_VERSION="4.5.1"
SAGE_BASE_URL="http://mira.sunsite.utk.edu/sagemath/src/"
SAGE_FILENAME="sage-4.5.1.tar"

import os,sys,re
from string import Template
from subprocess import Popen

# Check our os
if not os.name=="posix":
  print "This script will only work on a linux machine!"
  sys.exit(1)

# List of all python packages that can be installed with EasyInstall
PYTHON_PACKAGES = """numexpr
pyrex
http://pytables.org/svn/pytables/branches/std-2.2
configobj
pexpect
xlrd
xlwt
sympy
elementtree
django
pil"""
PYTHON_PACKAGES = PYTHON_PACKAGES.split("\n")

# List of all packages that need to be installed if we're on a debian variant
DEBIAN_PACKAGES = """libhdf5-openmpi-dev"""
DEBIAN_PACKAGES = DEBIAN_PACKAGES.split("\n")

# List of all packages that need to be installed if we're on a RHEL variant
RHEL_PACKAGES = """hdf5-devel
gcc-c++
gtk2-devel
scons
fftw3-devel
fftw3
freetype-devel
castor-ns-client
castor-rfio-client
python-devel
scipy
mysql-devel
php
httpd
httpd-devel
boost-devel
qt4-devel
qt4-mysql
qt4
swig
sip
castor-devel
openafs-devel
gsl-devel
ruby
ruby-devel
ncurses-devel
ncurses
hdf5-devel
hdf-devel
intltool"""
RHEL_PACKAGES = RHEL_PACKAGES.split("\n")

def get_architecture():
  import platform
  return platform.architecture()[0]
def get_prefix():
  arch_name = ""
  if get_architecture() == "64bit":
    arch_name = "x86_64"
  elif get_architecture() == "32bin":
    arch_name = "x86"

  HOME = os.environ["HOME"]
  prefix = os.path.join(os.path.abspath(HOME),"local",arch_name)

  return prefix

def make_directories():
  prefix = get_prefix()
  os.system("mkdir -p %s" %prefix)

def install_os_packages(thisos):
  print "Installing OS Packages"
  thisos = thisos.upper()
  if thisos == "RHEL":
    PACKAGE_LIST = RHEL_PACKAGES
    print "Installing RHEL Packages"
    return Popen(["sudo","yum","install","-y"]+PACKAGE_LIST).wait()
  elif thisos == "UBUNTU":
    print "Installing Ubuntu Packages"
    PACKAGE_LIST = DEBIAN_PACKAGES
    return Popen(["sudo","apt-get","install","-y"]+PACKAGE_LIST).wait()
  return -1

# Extract and install sage
def install_sage():
  print "Downloading and installing sage"

  # Download Sage
  DOWNLOAD = SAGE_BASE_URL+SAGE_FILENAME
  OUTPUT = os.path.join(get_prefix(),"downloads",SAGE_FILENAME)
  DOWNLOAD_DIRECTORY = os.path.join(get_prefix(),"downloads")

  if not os.path.exists(OUTPUT):
    os.system("mkdir -p %s" % DOWNLOAD_DIRECTORY)
    command = "wget -O %s %s" % (OUTPUT,DOWNLOAD)
    os.system(command)

  # Extract it
  os.chdir(DOWNLOAD_DIRECTORY)
  if not os.path.exists(os.path.join(DOWNLOAD_DIRECTORY,"sage-%s"%SAGE_VERSION)):
    command = "tar -xvf %s" % SAGE_FILENAME
    os.system(command)

  # Build it
  os.chdir("sage-%s"%SAGE_VERSION)
  os.system("make -j4")
  os.chdir(DOWNLOAD_DIRECTORY)

  SAGE_DESTINATION = os.path.join(get_prefix(),"sage")
  os.system("rm -rf %s"%SAGE_DESTINATION)
  os.system("mv %s %s"%("sage-%s"%SAGE_VERSION,SAGE_DESTINATION))

def install_root():
  ROOTSYS=os.path.join(get_prefix(),"root")
  DOWNLOAD_DIRECTORY = os.path.join(get_prefix(),"downloads")
  OUTPUT = os.path.join(DOWNLOAD_DIRECTORY,ROOT_FILENAME)

  # Download the source file
  os.chdir(DOWNLOAD_DIRECTORY)
  if not os.path.exists(OUTPUT):
    command = "wget -O %s %s"%(OUTPUT,ROOT_BASE_URL+"/"+ROOT_FILENAME)
    os.system(command)

  # Extract it
  if not os.path.exists(os.path.join(DOWNLOAD_DIRECTORY,"root")):
    os.system("tar -xzvf %s"%(ROOT_FILENAME))

  # Move it
  os.system("mv %s %s"%(os.path.join(DOWNLOAD_DIRECTORY,"root"),ROOTSYS))

  # Build it
  os.chdir(ROOTSYS)
  status = os.system("./configure --fail-on-missing --enable-python --enable-mathmore --enable-mathcore --enable-gdml --enable-cintex  --enable-genvector --enable-reflex --enable-roofit --enable-table --enable-asimage --enable-unuran --enable-tmva --enable-memstat --enable-editline --enable-xft --enable-builtin-freetype --with-python-incdir=%s"%(os.path.join(get_prefix(),"sage","local","include","python2.6")))
  if not status == 0: return status
  return os.system("make -j4")

def install_python_packages():
  # Requires that sage is already installed
  EASY_INSTALL = os.path.join(get_prefix(),"sage","local","bin","easy_install")

  for package in PYTHON_PACKAGES:
    status = Popen([EASY_INSTALL,package]).wait()
    if not status == 0: return status

  return 0
  
def generate_bash():
  t = Template("""
# So this file can be sourced multiple times
source /etc/bashrc

# ROOT variables
export ROOTSYS=$prefix/root

# SAGE variables
export SAGESYS=$prefix/sage

# CMSSW

# PATH, etc
export PATH=$$ROOTSYS/bin:$$PATH
export PATH=$$SAGESYS/local/bin:$$PATH
export LD_LIBRARY_PATH=$$ROOTSYS/lib
export LD_LIBRARY_PATH=$$SAGESYS/local/lib:$$LD_LIBRARY_PATH
export PYTHONPATH=$$ROOTSYS/lib
export CPATH=$$ROOTSYS/include:$$SAGESYS/local/include
export LIBRARY_PATH=$$ROOTSYS/lib:$$SAGESYS/local/lib
  """)

  return t.substitute(prefix=get_prefix())

def write_bash():
  bash = generate_bash()
  filename = os.path.join(get_prefix(),"software.sh")
  f = open(filename,"w")
  f.write(bash)

def create_new_environment():
  SAGESYS = os.path.join(get_prefix(),"sage")
  os.environ["LD_LIBRARY_PATH"] = os.path.join(SAGESYS,"local","lib")
  os.environ["PATH"] = os.path.join(SAGESYS,"local","bin") + ":/usr/bin:/bin:/usr/local/bin"
  os.environ["PYTHONPATH"] = ""
  os.environ["LIBRARY_PATH"] = os.path.join(SAGESYS,"local","lib") 

#print get_prefix()
# Figure out which OS we have
thisos = ""
if os.path.exists("/etc/redhat-release"):
  thisos="RHEL"
elif os.path.exists("/etc/lsb-release"):
  thisos="UBUNTU"

# Install OS Packages
status = install_os_packages(thisos)
if not status == 0:
  print "Failed to install OS packages.  If you're on SLC5 or some other RHEL box, check that the DAG repository is enabled, or make sure that you're running as root. Exiting"
  sys.exit(status)

# Make the directories for the analysis software
make_directories()

# Install Sage
install_sage()

# Setup the environment to pull in the new python instance
create_new_environment()

# Install python packages
status = install_python_packages()
if not status == 0:
  print "Failed to install Python packages. Exiting."
  sys.exit(status)

# Install ROOT
install_root()

# Write out the generated environment file
write_bash()
