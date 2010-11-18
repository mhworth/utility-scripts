export VO_CMS_SW_DIR=/home/mhollin3/cmssw
mkdir -p $VO_CMS_SW_DIR
export SCRAM_ARCH=slc5_ia32_gcc434
wget -O $VO_CMS_SW_DIR/bootstrap.sh http://cmsrep.cern.ch/cmssw/cms/bootstrap.sh
sh -x $VO_CMS_SW_DIR/bootstrap.sh setup -path $VO_CMS_SW_DIR -arch $SCRAM_ARCH >& $VO_CMS_SW_DIR/bootstrap_$SCRAM_ARCH.log
source $VO_CMS_SW_DIR/$SCRAM_ARCH/external/apt/0.5.15lorg3.2-cms2/etc/profile.d/init.sh
apt-get update
apt-get install external+fakesystem+1.0 external+fakesystem+1.0-cms
apt-get install cms+cmssw+CMSSW_3_5_2
