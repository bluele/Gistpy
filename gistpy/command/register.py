#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy import Auth, Query
from gistpy.command import SimpleCommand
from gistpy.errors import UnauthorizedUser
from gistpy.constant import APP_SCOPES, APP_NOTE, APP_TOKEN, GITHUB_AUTHORIZATION_PATH


class Register(SimpleCommand):

    def __init__(self, args):
        self.auth = Auth(args.user, args.password)
        self.init_query()
        self.init_payload()
        
    def init_query(self):
        self.query = Query(filters=[self.auth.to_basicauth()])
        self.build_query()

    def build_query(self):
        self.query.concat_path(GITHUB_AUTHORIZATION_PATH)

    def build_payload(self):
        self.payload["scopes"] = APP_SCOPES
        self.payload["note"] = APP_NOTE

    def invoke(self):
        try:
            access_token = self.auth.get_access_token_api()
        except UnauthorizedUser:
            print u"Try to register this appliation."
            print u"*" * 50
        except Exception:
            raise
        else:
            print u"You have already registered your account with this application."
            print u"Your access_token is {0}".format(access_token)
            return access_token

        response = self.query.do_POST(
                                payload=self.payload,
                                )
        return self.on_receive(response)

    def on_receive(self, response):
        print u"You successfully register your account with this application."
        print u"Your access_token is {0}\n".format(response["token"])
        print u"Please do `export {0}={1}`.".format(APP_TOKEN, response["token"])
        return response

