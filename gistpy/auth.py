#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy.query import Query
from gistpy.errors import UnSetUserKeyError, UnauthorizedUser
from gistpy.constant import APP_NAME, APP_USER, APP_PASSWORD, APP_TOKEN, GITHUB_AUTHORIZATION_PATH
from restkit import BasicAuth
import os

__all__ = ("Auth",)


class Auth(object):

    def __init__(self, user=None, password=None):
        self._user = user
        self._password = password

    def get_access_token_environ(self):
        return os.environ[APP_TOKEN]

    def get_access_token_api(self):
        response = self._get_authorization_list()
        for auth in response:
            if auth["app"]["name"] == u"{0} (API)".format(APP_NAME):
                return auth["token"]
        else:
            raise UnauthorizedUser(
            u"""
            Your authorization on github was not found.
            Please do `$ gistpy register`.
            """)

    def get_access_token(self, is_api=False):
        try:
            return self.get_access_token_environ()
        except:
            print u"'os.environ[\"{0}\"]' was not found.\n".format(APP_TOKEN)
        if not is_api:
            raise UnSetUserKeyError(u"You should do `export {0}=your_access_token`".format(APP_TOKEN))
        print u"Try to fetch your authorization on github.\n"
        return self.get_access_token_api()

    def _get_authorization_list(self):
        query = Query(filters=[self.to_basicauth()])
        query.concat_path(GITHUB_AUTHORIZATION_PATH)
        return query.do_GET()

    def to_basicauth(self):
        return BasicAuth(self.user, self.password)

    def get_user_key(self):
        if self._user is not None:
            return self._user
        user = os.environ.get(APP_USER)
        if user:
            return user
        raise UnSetUserKeyError("You should do `export {0}=user`".format(APP_USER))

    def get_password_key(self):
        if self._password is not None:
            return self._password
        password =  os.environ.get(APP_PASSWORD)
        if password:
            return password
        raise UnSetUserKeyError("You should do `export {0}=password`".format(APP_PASSWORD))

    def get_key(self):
        return self.get_user_key(), self.get_password_key()

    user = property(get_user_key)
    password = property(get_password_key)

