#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Application
# =============================== #
DEBUG = False
APP_NAME = "Gistpy"
DEFAULT_GIST_NAME = "gist"
ALLOW_SCHEME_LIST = (u"https",)
ALLOW_HOST_LIST = (u"api.github.com", u"gist.github.com")

# Github
# =============================== #
GITHUB_URL = "https://api.github.com"
GISTS_PATH = "gists"
GITHUB_AUTHORIZATION_PATH = "authorizations"

# Authorization
# =============================== #
APP_USER = "{0}_USER".format(APP_NAME.upper())
APP_PASSWORD = "{0}_PASSWORD".format(APP_NAME.upper())
APP_TOKEN = "{0}_TOKEN".format(APP_NAME.upper())
APP_SCOPES = ["gist"]
APP_NOTE = APP_NAME

# command
# =============================== #
CREATE = "create"
GET = "get"
DELETE = "delete"
EDIT = "edit"
LIST = "list"
REGISTER = "register"
CREATE_STDIN = "create_stdin"
