#!/usr/bin/python

"""Installs all python packages that I would like to have on all machines.

(Linux Only)"""

from shellscripts import *
import os,sys,re


#List of all pre-existing packages for ubuntu
UBUNTU_PACKAGES = ["python", \
		   "python-dev", \
		   "python2.4", \
		   "python2.4-dev", \
		   "python-pexpect", \
		   "python-imaging", \
		   "python-reportlab-accel", \
		   "python-reportlab", \
	 	   "python-ldap", \
		   "python-epydoc", \
		   "python-twisted-conch", \
		   "python-twisted-words", \
		   "python-twisted-names", \
		   "python-twisted-mail", \
		   "python-twisted-news", \
		   "python-twisted-runner", \
		   "python-dateutil", \
		   "python-scipy", \
		   "python-soappy", \
		   "python-serial", \
		   "python-soappy", \
		   "python-scapy", \
		   "python-rpm", \
		   "python-cairo", \
		   "python-genetic", \
		   "python-gpod", \
		   "python-htmlgen", \
		   "python-magic", \
		   "python-gpod", \
		   "python-pyopenssl", \
		   "python-pyorbit", \
		   "python-pysqlite2", \
		   "python-sip4", \
		   "python-subversion", \
		   "python-xml", \
		   "python-asterisk", \
		   "python-comedilib", \
		   "python-cxx", \
		   "python-elementtree", \
		   "python-excelerator", \
		   "python-fuse", \
		   "python-imdbpy", \
		   "python-ldaptor", \
		   "python-ll-core", \
		   "python-matplotlib", \
		   "python-musicbrainz2", \
		   "python-networkx", \
		   "python-opengl", \
		   "python-numpy", \
		   "python-omniorb2-omg", \
		   "python-openid", \
		   "python-pastescript", \
		   "python-pygments", \
		   "python-simpy", \
		   "python-simpleparse", \
		   "python-soya", \
		   "python-sympy", \
		   "python-urlgrabber", \
		   "python-visual", \
		   "python-wxgtk2.8", \
		   "python-zodb"]

#A list of packages to setup using setuptools
SETUPTOOL_PACKAGES = ["xlrd"]

def install_setuptools():
	EZSETUP_URL = "http://peak.telecommunity.com/dist/ez_setup.py"
	EZSETUP_DEST = os.path.join("/tmp","ez_setup.py")

	#Download ez_setup
	wget_command = "wget %s -O %s" % (EZSETUP_URL,EZSETUP_DEST)
	wget = run(wget_command)
	wget.wait()

	#Setup ez_setup so we can download the packages easily that aren't available via "normal" distributions
	ez_setup_command = "python %s" % EZSETUP_DEST
	ez_setup = run(ez_setup_command)
	ez_setup.wait()
	#Delete the temp file
	os.remove(EZSETUP_DEST)

def install_ubuntu_packages():
	""
	packages = ""
	for package in UBUNTU_PACKAGES:
		packages += (package + " ")
	aptget_command = "apt-get install %s" % packages
	aptget = run(aptget_command)
	aptget.wait()
	
def install_setuptools_packages():
	""
	processes = []
	for package in SETUPTOOL_PACKAGES:
		ezsetup = run("easy_install %s" % package)
		processes.append(ezsetup)
	
	for process in processes:
		process.wait()

#If setuptools ain't there, install it
try:
	import setuptools
except:
	install_setuptools()

# Now to install the Ubuntu packages
install_ubuntu_packages()

#and the setuptools packages
install_setuptools_packages()

