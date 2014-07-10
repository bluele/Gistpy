#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy.auth import Auth
from gistpy.query import Query
from gistpy.dispatch import Dispatcher
from gistpy.argbuilder import ParserBuilder


def main():
    Dispatcher().dispatch()
