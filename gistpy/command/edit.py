#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy.command import SimpleCommand
from gistpy.constant import GISTS_PATH
from os.path import basename, abspath


class Edit(SimpleCommand):

    def __init__(self, args):
        self.gistid = args.gistid
        self.files = map(abspath, args.files)
        self.description = args.description
        self.init_query()
        self.init_payload()

    def build_query(self):
        self.query.concat_path(GISTS_PATH, self.gistid)
        
    def build_payload(self):
        if self.description is not None:
            self.payload["description"] = self.description
        for path in self.files:
            name = basename(path)
            self.payload.setdefault("files", dict()).setdefault(name, dict())
            self.payload["files"][name]["content"] = open(path, "rb").read()
        
    def invoke(self):
        response = self.query.do_PATCH(payload=self.payload)
        return self.on_receive(response)
    
    def on_receive(self, response):
        self.clipboard_set(response["html_url"])
        print u"EDIT ====> {0}".format(response["html_url"])
        return response
