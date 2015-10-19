#!/usr/bin/env python3
import sys
import os.path
import argparse
import shlex
import subprocess


class Proximac:
    version = '2.1'

    def __init__(self):
        self.command = Command()
        self.description = "Proximac v%(version)s is a command-line open-source \
                alternative to Proxifier."  % {'version': self.version}
        self.usage = '''\
proximac [-h] <command> [<args>]

commands:
    start    start proximac
    stop     stop proximac
'''
        self.default_error = "Unrecognized command"
        self.initialize()

    def initialize(self):
        self.parser = argparse.ArgumentParser(
            description=self.description,
            usage=self.usage
        )
        self.parser.add_argument('command', help='subcommand to run')
        args = self.parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print(self.default_error)
            self.parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def start(self):
        parser = argparse.ArgumentParser(
            prog="proximac start",
            description="start proximac"
        )
        parser.add_argument('-c', '--config',
                            help="path of configuration file that is written in JSON")
        parser.add_argument('-d', '--daemon', action="store_true", help="daemon mode")
        args = parser.parse_args(sys.argv[2:])

        if len(sys.argv) < 3:
            parser.print_help()
        else:
            if self.command.is_kext_load():
                self.command.start(args.config, args.daemon)
            else:
                sys.exit(1)

    def stop(self):
        if len(sys.argv) > 2:
            self.parser.print_help()
        else: 
            self.command.stop()


class Command:
    NOT_VALID_PATH = 127

    def run(self, args):
        return_code = 0

        if sys.hexversion < 0x30500f0:
            return_code = subprocess.call(args)
        else:
            cp = subprocess.run(args)
            return_code = cp.returncode

        return return_code

    def is_kext_load(self):
        cmd_str = "sudo kextload /usr/local/proximac/proximac.kext"
        args = shlex.split(cmd_str)
        return_code = self.run(args)

        if return_code != 0:
            print('''\
Kernel extension cannot be loaded! \
Maybe it is already loaded so you have to unload it first. \
Or installing third-party kext is not allowed on your OS.''')
            return False
        else:
            return True

    def start(self, config, daemon=False):
        return_code = 0

        if not os.path.isfile(config):
            print("This is not a valid path.")
            return_code = self.NOT_VALID_PATH
        else:
            args = ['/usr/local/proximac/proximac-cli', '-c', config]
            if daemon:
                args.append('-d')
            return_code = self.run(args)

        sys.exit(return_code)

    def stop(self):
        cmd_str = "killall proximac-cli"
        args = shlex.split(cmd_str)
        return_code = self.run(args)

        if return_code != 0:
            print("Proximac may not be started or may be killed accidentally.")
        sys.exit(return_code)


if __name__ == '__main__':
    Proximac()
