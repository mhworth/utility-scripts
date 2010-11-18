# Make sure you are up-to-date
yum update

# Install NX rpm dependencies
yum install expect nc

# Grab a Freenx package

# Use this package for FC2, FC3, FC4, and xorg based distributions
wget http://fedoranews.org/contributors/rick_stout/freenx/freenx-0.4.4-2.fdr.0.noarch.rpm

# Use this package for FC1, RH9, RHEL3 or XFree86 based distributions
# wget http://fedoranews.org/contributors/rick_stout/freenx/freenx-0.4.4-2.rh.0.noarch.rpm

# Next, grab an nx package

# This package was built on FC4
wget http://fedoranews.org/contributors/rick_stout/freenx/nx-1.5.0-4.FC4.1.i386.rpm

# This package was built on FC3
# wget http://fedoranews.org/contributors/rick_stout/freenx/nx-1.5.0-4.FC3.1.i386.rpm

# This package was built on FC2
# wget http://fedoranews.org/contributors/rick_stout/freenx/nx-1.5.0-4.FC2.1.i386.rpm

# Use this package if you are using FC1, RH9, RHEL3 or a Redhat compatible
# distribution using XFree86
# wget http://fedoranews.org/contributors/rick_stout/freenx/nx-1.5.0-4.FC1.1.i386.rpm


# Source rpm's
# wget http://fedoranews.org/contributors/rick_stout/freenx/freenx-0.4.4-2.fdr.0.src.rpm
# wget http://fedoranews.org/contributors/rick_stout/freenx/freenx-0.4.4-2.rh.0.src.rpm
# wget http://fedoranews.org/contributors/rick_stout/freenx/nx-1.5.0-4.FC4.1.src.rpm
# wget http://fedoranews.org/contributors/rick_stout/freenx/nx-1.5.0-4.FC1.1.src.rpm
# wget http://fedoranews.org/contributors/rick_stout/freenx/md5sum

# Install the RPM's
#rpm -Uvh nx-1.5.0-4.FC4.1.i386.rpm
#rpm -Uvh freenx-0.4.4-2.fdr.0.src.rpm

#SERVER SETUP IS DONE! The RPM takes care of the required setup.

