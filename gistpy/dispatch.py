#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy.argbuilder import ParserBuilder
from gistpy.util import debug_print
from gistpy.constant import APP_NAME
import argparse
import traceback
import os


class Dispatcher(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog=APP_NAME)
        if not os.isatty(os.sys.stdin.fileno()):
            # exists stdin
            return ParserBuilder(self.parser).build(ParserBuilder._CreateStdinBuilder)
        self.init_command()

    def init_command(self):
        subparsers = self.parser.add_subparsers(
                            title="commands",
                            help="command help"
                            )
        ParserBuilder(subparsers).build()

    def dispatch(self, argv=None):
        args = self.parser.parse_args(argv)
        try:
            debug_print(args.func(args))
        except Exception, emg:
            print emg
            debug_print(traceback.format_exc())

