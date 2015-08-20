#!/usr/bin/python
import commands
check_libuv_result = commands.getstatusoutput('ls /usr/local/lib/libuv.a')
if check_libuv_result[0] != 0:
	print 'Please install libuv fisrt!\n\
	run "brew install libuv"'

download_result = commands.getstatusoutput('curl -o proximac.zip https://raw.githubusercontent.com/proximac-org/proximac-install/master/proximac.zip')
if download_result[0] != 0:
	print 'Download remote resources failed!'
	exit()

print 'Resources has been downloaded!'

unzip_result = commands.getstatusoutput('unzip -o proximac.zip')
print unzip_result
if unzip_result[0] != 0:
	print 'Unzip install files failed! Check your permission on this folder!'
	exit()

print 'Now change kernel extension\'s owner'
print 'Please enter your password to obtain root priviledge'

chown_result = commands.getstatusoutput('sudo chown -R root:wheel proximac.kext')
if chown_result[0] != 0:
	print 'command execution failed!'
	exit()

print 'Proximac is successfully installed!'
