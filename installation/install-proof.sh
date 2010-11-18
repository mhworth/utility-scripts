#!/bin/bash

###
# XROOTD Setup
###

# Create user
/usr/sbin/adduser xrootd
mkdir /var/log/xrootd
chown xrootd /var/log/xrootd

# make xrootd config
MASTER=pccmsbrm4
OSSPATH=/data/xrootd/
OLBPATH=/data/xrootd/
mkdir $OSSPATH
mkdir $OLBPATH
chown xrootd $OSSPATH $OLBPATH

echo "Installing xrootd config file with MASTER=$MASTER, OSSPATH=$OSSPATH, OLBPATH=$OLBPATH"

cat > /etc/xrootd.cf <<End-of-conf
# xrootd.cf

# Network Setup
xrd.port 1094
olb.port 3121

# Setup the file system
xrootd.fslib /opt/root/lib/libXrdOfs.so
if exec olbd
    xrd.sched mint 10 maxt 100 avlt 20
fi


if $MASTER
    ofs.redirect remote
    ofs.forward all
else
    ofs.redirect target
fi

# Define exports
all.export $OLBPATH
all.export $OSSPATH

# OSS/OLB paths
oss.path $OSSPATH r/w
olb.path rw $OLBPATH

# Set the roles
if $MASTER
  all.role manager
else
  all.role server
fi

# Configure OLB
olb.subscribe $MASTER 3121
odc.manager $MASTER 3121
olb.delay startup 30
olb.space 20g 1g

# Configure the xrootd protocol
if exec xrootd
  xrd.protocol xproofd:1093 /opt/root/lib/libXrdProofd.so
fi

xpd.rootsys /opt/root
xpd.workdir $OLBPATH
xpd.intwait 20
xpd.allow $MASTER
xpd.poolurl root://$MASTER
xpd.namespace /home/xrootd/proofpool

# Define workers
xpd.worker worker pccmsbrm[4,5] port=1093
End-of-conf

echo "Installing startup scripts into /etc/init.d"
# Install start script
#wget -O /etc/init.d/xrootd http://wisconsin.cern.ch/~nengxu/xrootd_install/xrootd
#wget -O /etc/init.d/olbd http://wisconsin.cern.ch/~nengxu/xrootd_install/olbd
cp xrootd /etc/init.d/xrootd
cp olbd /etc/init.d/olbd
chmod 755 /etc/init.d/xrootd
chmod 755 /etc/init.d/olbd

###
# Starting Services
###
/etc/init.d/xrootd start
/etc/init.d/olbd start
