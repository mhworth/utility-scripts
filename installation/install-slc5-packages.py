from subprocess import Popen

PACKAGES="""gcc-c++
gtk2-devel
scons
fftw3-devel
fftw3
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
PACKAGE_LIST=PACKAGES.split("\n")

Popen(["yum","install","-y"]+PACKAGE_LIST).wait()
