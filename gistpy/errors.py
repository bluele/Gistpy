#!/usr/bin/env python
# -*- coding: utf-8 -*-

from restkit import Unauthorized


class GistpyError(Exception):
    pass


class UnSetUserKeyError(GistpyError):
    pass


class UnauthorizedUser(GistpyError):
    pass