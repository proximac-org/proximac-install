#!/usr/bin/python
import commands,sys,os
argc = len(sys.argv)

if argc == 3 and sys.argv[1] == 'start':
	kextload_result = commands.getstatusoutput('sudo kextload /usr/local/proximac/proximac.kext')
	if kextload_result[0] != 0:
		print 'Kernel extension cannot be loaded! Maybe it is already loaded so you have to unload it first. Or installing third-party kext is now allowed on your OS.'
		exit()

	cmd_str = '/usr/local/proximac/proximac-cli -c ' + sys.argv[2]
	print cmd_str
	os.system(cmd_str)
	exit()


if argc == 2 and sys.argv[1] == 'stop':
	kill_result = commands.getstatusoutput('killall proximac-cli')
	if kill_result[0] != 0:
		print 'Proximac may not be started or may be killed accidentally'
		exit()
	exit()

print 'proximac v2.1\n\
Usage:\n\
start Proximac:\n\
proximac start [path of your config file]\n\
stop Proximac:\n\
proximac stop '
