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

if argc == 2 and sys.argv[1] == 'stop':
	os.system('killall proximac-cli')
