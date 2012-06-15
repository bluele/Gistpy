#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy import Auth, Query
from gistpy.command import SimpleCommand
from gistpy.constant import GISTS_PATH, DEFAULT_GIST_NAME
from os.path import basename, abspath
import sys

__all__ = ("Create", "CreateStdin")


class Create(SimpleCommand):

    def __init__(self, args):
        self.files = map(abspath, args.files)
        self.init(args)
        
    def init(self, args):
        self.is_public = args.private
        self.description = args.description or u""
        self.payload = dict()
        self.is_anonymous = args.anonymous
        self.init_query()
        self.init_payload()
        
    def build_payload(self):
        self.payload["description"] = self.description
        self.payload["public"] = self.is_public
        self.payload["files"] = dict()
        for fpath in self.files:
            fname = basename(fpath)
            self.payload["files"].setdefault(fname, dict())
            self.payload["files"][fname]["content"] = open(fpath, "rb").read()

    def init_query(self):
        access_token = None
        if not self.is_anonymous:
            access_token = Auth().get_access_token(is_api=True)
        self.query = Query(access_token=access_token)
        self.build_query()

    def build_query(self):
        self.query.concat_path(GISTS_PATH)

    def invoke(self):
        response = self.query.do_POST(payload=self.payload)
        return self.on_receive(response)

    def on_receive(self, response):
        self.clipboard_set(response["html_url"])
        print "CREATE ====> {0}".format(response["html_url"])
        for fpath in self.files:
            print fpath
        return response


class CreateStdin(Create):

    def __init__(self, args):
        self.filename = args.filename or DEFAULT_GIST_NAME
        self.init(args)

    def build_payload(self):
        self.payload["description"] = self.description
        self.payload["public"] = self.is_public
        self.payload["files"] = {self.filename:{"content":sys.stdin.read()}}

    def on_receive(self, response):
        self.clipboard_set(response["html_url"])
        print "CREATE ====> {0}".format(response["html_url"])
        print self.filename
        return response
