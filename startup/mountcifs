#!/usr/bin/python
import os,sys,re
import shutil
from optparse import OptionParser
from subprocess import Popen,PIPE

def install():
	filename = __file__
	filepath = os.path.abspath(__file__)
	dest = os.path.join("/etc/init.d",filename)
	shutil.copyfile(filepath,dest)
	os.chmod(dest,os.X_OK)
	os.symlink(dest, "/etc/rc0.d/K02mountcifs")
	os.symlink(dest, "/etc/rc6.d/K02mountcifs")

def uninstall():
	filename = __file__
        filepath = os.path.abspath(__file__)
        dest = os.path.join("/etc/init.d",filename)
	os.remove(dest)
	os.remove("/etc/rc0.d/K02mountcifs")
	os.remove("/etc/rc6.d/K02mountcifs")

def stop():
	mount = Popen("mount -t cifs| cut -d\  -f3",shell=True,stdout=PIPE)
	mount.wait()
	MOUNTED_CIFS_DIRS = []
	for line in mount.stdout:
		MOUNTED_CIFS_DIRS.append(line.strip())

	for mount in MOUNTED_CIFS_DIRS:
		print "Unmounting %s" % mount
		umount = Popen("umount.cifs -l %s" % mount, shell=True)
		
def start():
	mount_all()
	
def status():
	mounts = list_mounts()	
	for m in mounts:
		print m

def list_mounts():
	
	mount = Popen("mount -t cifs| cut -d\  -f3",shell=True,stdout=PIPE)
	mount.wait()
	mounts = []
	for line in mount.stdout:
		mounts.append(line.strip())

	return mounts	

def check_for_cifs_host(host,timeout=3):
	"""Tries to connect to the samba port, which is 445.  If successful,
we can assume that the server exists so we can connect to it.  If not, then we can't connect to it."""
	import socket
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(timeout)
	success = False
	try:
		s.connect((host,445))
		success=True
	except:
		success=False
	return success

def parse_mount_list(conf):
	"""Returns a list of dicts, which contain the following:
	(share,mount-point,options)
	"""
	f = open(conf)
	ret = []
	for line in f:
		info = line.split(" ")
		if not (len(info) >= 3):
			continue
		info_parsed = {}
		info_parsed['share'] = info[0].strip()
		info_parsed['mountpoint'] = info[1].strip()
		options = ""
		for o in info[2:]:
			options += o + " "
		options = options.strip()
		info_parsed['options'] = options.strip() 
		ret.append(info_parsed)

	return ret

def mount(info):
	
	mounts = list_mounts()
	if info['mountpoint'] in mounts:
		print "Mountpoint %s already in use!" % info['mountpoint']
		return
	r = re.compile(r"//(.*)/(.*)")
	m = r.match(info["share"])
	host = m.groups()[0]
	if not (check_for_cifs_host(host)):
		print "Server %s not found" % host
		return
	command = "mount.cifs %s %s -o%s" % (info["share"],info['mountpoint'],info['options'])
	print "Running command %s" % command
	mount = Popen(command,shell=True)
	mount.wait()

def mount_all():
	"""Looks in the home directory of the user to mount all of their desired mounts"""
	HOME = os.environ["HOME"]
	if os.path.exists(os.path.join(HOME,".mountcifs")):
		info_list = parse_mount_list(os.path.join(HOME,".mountcifs"))
		for info in info_list:
			mount(info)


if __name__ == "__main__":
	parser = OptionParser()
	
	(options,args) = parser.parse_args()

	if args[0] == "install":
		print "mountcifs: Installing"
		install()
	elif args[0] == "uninstall":
		print "mountcifs: Uninstalling"
		uninstall()
	elif args[0] == "stop":
		print "mountcifs: Unmounting all CIFS mounts"
		stop()
	elif args[0] == "start":
		print "mountcifs: Starting"
		start()
	elif args[0] == "status":
		print "mountcifs: Listing mounted CIFS volumes"
		status()
	elif args[0] == "check":
		print "Checking for cifs host %s" % args[1]
		ret = check_for_cifs_host(args[1])
		print ret
	
