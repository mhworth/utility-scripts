#sudo apt-get install libxpm-dev xserver-xorg-dev libxft-dev libxext-dev build-essential mysql-client libmysql++-dev python2.5-dev libgsl0-dev
echo "Don't forget: you probably want to run install-slc5-packages.sh or the ubuntu equivalent if you want to run this!  That will install all of the necessary packages to build successfully"


PYTHON_INCLUDE=/data2/hollings/software/sage-4.4.4/local/include/python2.6

CORE_OPTS="--fail-on-missing --enable-python --enable-mathmore --enable-mysql\
 --enable-rfio --enable-mathcore --enable-gdml --enable-cintex\
 --enable-genvector --enable-reflex --enable-roofit --enable-table\
 --enable-asimage --enable-unuran --enable-tmva --enable-ruby\
 --enable-memstat --enable-editline --enable-xft --with-python-incdir=$PYTHON_INCLUDE"
 
#CERN_OPTS="--enable-afs --enable-castor "

OPTS="$CORE_OPTS $CERN_OPTS"

./configure $OPTS
