#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from gistpy.constant import ALLOW_SCHEME_LIST, ALLOW_HOST_LIST
from urlparse import urlparse
import argparse
import sys


class GistAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        self.parser = parser
        self.valid_values(values)
        setattr(namespace, self.dest, self.get_id(values))

    def get_id(self, values):
        def strip_path(path):
            return path.strip(u"/").split(u"/")[-1]
        return strip_path(urlparse(values).path)

    def valid_values(self, values):
        if len(values) == 0:
            self.parser.print_help()
            sys.exit(1)
