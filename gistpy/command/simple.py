#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy import Auth, Query
from gistpy.util import clipboard_set
from gistpy.errors import UnSetUserKeyError, UnauthorizedUser


class SimpleCommand(object):

    def init_query(self):
        try:
            self.query = Query(access_token=Auth().get_access_token())
        except (UnSetUserKeyError, UnauthorizedUser):
            self.query = Query()
        self.build_query()
        
    def init_payload(self):
        self.payload = dict()
        self.build_payload()
        
    def build_query(self):
        pass
        
    def build_payload(self):
        pass

    def invoke(self):
        raise NotImplementedError()

    def on_receive(self, response):
        raise NotImplementedError()

    def clipboard_set(self, text):
        try:
            clipboard_set(text)
        except:
            print u"Can't store text in the clipboard."

