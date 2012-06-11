#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy.command import SimpleCommand
from gistpy.constant import GISTS_PATH


class Delete(SimpleCommand):

    def __init__(self, args):
        self.gistid = args.gistid
        self.init_query()
        
    def build_query(self):
        self.query.concat_path(GISTS_PATH, self.gistid)
        
    def invoke(self):
        response = self.query.do_DELETE()
        self.on_receive(response)
        
    def on_receive(self, response):
        return response
