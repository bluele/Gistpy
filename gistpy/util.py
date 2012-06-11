#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from gistpy.clipboard import clipboard_set, clipboard_get
except:
    clipboard_set, clipboard_get = None, None
from gistpy.constant import DEBUG


def debug_print(text):
    if DEBUG:
        print text


