#!/usr/bin/python
import commands,os
check_libuv_result = commands.getstatusoutput('ls /usr/local/lib/libuv.a')
if check_libuv_result[0] != 0:
	print 'Please install libuv fisrt!\n\
	run "brew install libuv"'

mkdir_result = commands.getstatusoutput('mkdir -p /usr/local/proximac/')
if mkdir_result[0] != 0:
	print 'Cannot create fodler!'
	exit()

download_result = commands.getstatusoutput('cd /usr/local/proximac/ && curl -o proximac.zip https://raw.githubusercontent.com/proximac-org/proximac-install/master/proximac.zip')
if download_result[0] != 0:
	print 'Download remote resources failed!'
	exit()

download1_result = commands.getstatusoutput('cd /usr/local/bin && curl -o proximac https://raw.githubusercontent.com/proximac-org/proximac-install/master/proximac.py')
if download1_result[0] != 0:
	print 'Download remote resources failed!'
	exit()

chmod_result = commands.getstatusoutput('cd /usr/local/bin && chmod 777 proximac')
if chmod_result[0] != 0:
	print 'Cannot chage permission!'
	exit()

print 'Resources has been downloaded!'

unzip_result = commands.getstatusoutput('cd /usr/local/proximac/ && unzip -o proximac.zip')
if unzip_result[0] != 0:
	print 'Unzip install files failed! Check your permission on this folder!'
	exit()

print 'Now change kernel extension\'s owner'
print 'Please enter your password to obtain root priviledge'

chown_result = commands.getstatusoutput('cd /usr/local/proximac/ && sudo chown -R root:wheel proximac.kext')
if chown_result[0] != 0:
	print 'command execution failed!'
	exit()

os.system('cd /usr/local/proximac/ && rm -rf proximac.zip')
print 'Proximac is successfully installed!'
