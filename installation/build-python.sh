
#Install prerequisites
YUM_PACKAGES="tcl-devel tk-devel"
sudo yum install $YUM_PACKAGES

# Figure out whether we're 32 bit or 64 bit
if [ `uname -i` == "i386" ]; then
 #32 bit
 PREFIX=/nfs/software/local/x86
else
 #64 bit
 PREFIX=/nfs/software/local/x86_64
fi

# Configure
./configure --enable-shared --prefix=$PREFIX

# Build
make -j2

# Install
make install
