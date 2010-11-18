#!/usr/bin/python
"""
install-root.py
By Matt Hollingsworth

License: Public Domain

*Description*
This script will install root (http://root.cern.ch/) on your computer
by (optionally) downloading the lastest distribution and compiling it on your 
computer.

*Requirements*

All OS's:
* Python >= 2.4 (http://www.python.org/)
* Internet connection (or not, if you already have a root distribution)

Linux:

The script will try to tell you what you need to install if you don't have it,
but here is a (possibly incomplete) list.

* Basic compile tools such as make, autoconf, and gcc
* Lots of libraries that I'll list later

Windows:

* Visual C++ > 6.0 (insert link here)
* Lots of libraries

Usage: 

install-root.py [--download] [--download-version <version>] [--conf <file>] --rootsys <directory>

--conf specifies an ini-style file that tells the different arguments for the compile.

Example:

#root-conf.ini

# All values in this file are expanded in a shell-like way, i.e.,
# $HOME would put in your home directory

[args]
# Raw args to pass to the script.  If any of the generated args match one of these,
# then what is specified here overrides it
--prefix 
[with]
python-incdir= /usr/include/python2.5
python-libdir= /usr/lib

[enable]
# Enables root features
python

[disable]
# Disables root features
chirp

[define-env]
# Defines environment variables.  Pre-existing environment variables are also expanded.
ROOTSYS: $HOME/local/apps/root



"""
