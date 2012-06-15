#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy.command import SimpleCommand
from gistpy.constant import GISTS_PATH
from os.path import abspath, isdir, join
import os


class Get(SimpleCommand):

    def __init__(self, args):
        self.gistid = args.gistid
        dest_dir = abspath(args.destination_directory)
        if not isdir(dest_dir):
            raise OSError(u"{0} is not directory.".format(dest_dir))
        self.dest_dir = join(dest_dir, self.gistid)
        self.init_query()
        
    def build_query(self):
        self.query.concat_path(GISTS_PATH, self.gistid)

    def invoke(self):
        response = self.query.do_GET()
        return self.on_receive(response)

    def on_receive(self, response):
        print u"Get ====> {0}".format(response["html_url"])
        # create directory
        os.makedirs(self.dest_dir)
        for name, item in response["files"].iteritems():
            path = join(self.dest_dir, name)
            print path
            with open(path, "wb") as f:
                f.write(item["content"])
        return response

