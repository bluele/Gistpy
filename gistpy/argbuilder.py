#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy.command import Create, Get, Edit, Delete, Register, CreateStdin
from gistpy.argaction import GistAction
from gistpy.constant import CREATE, GET, EDIT, DELETE, REGISTER, CREATE_STDIN


class ParserBuilder(object):

    def __init__(self, parser):
        self.parser = parser

    def build(self, builder=None):
        if builder is not None:
            builder(self.parser).build()
            return
        for attr in dir(self):
            if not attr.startswith("_") and attr.endswith("Builder"):
                builder = getattr(self, attr)
                parser = self.parser.add_parser(builder.command)
                builder(parser).build()


    class _SimpleBuilder(object):
        command = None

        def __init__(self, parser):
            self.parser = parser

        def build(self):
            raise NotImplementedError()


    class _CreateStdinBuilder(_SimpleBuilder):
        command = CREATE_STDIN

        def build(self):
            self.parser.add_argument("filename", nargs='?')
            self.parser.add_argument("-p", "--private", action="store_false")
            self.parser.add_argument("-a", "--anonymous", action="store_true")
            self.parser.add_argument("-d", "--description", nargs='?')
            self.parser.set_defaults(func=lambda *args:CreateStdin(*args).invoke())


    class CreateBuilder(_SimpleBuilder):
        command = CREATE

        def build(self):
            # default: public
            self.parser.add_argument("files", nargs='+')
            self.parser.add_argument("-p", "--private", action="store_false")
            self.parser.add_argument("-a", "--anonymous", action="store_true")
            self.parser.add_argument("-d", "--description", nargs='?')
            self.parser.set_defaults(func=lambda *args:Create(*args).invoke())


    class GetBuilder(_SimpleBuilder):
        command = GET

        def build(self):
            self.parser.add_argument("gistid", action=GistAction)
            self.parser.add_argument("destination_directory", nargs='?', default=u'.')
            self.parser.set_defaults(func=lambda *args:Get(*args).invoke())


    class EditBuilder(_SimpleBuilder):
        command = EDIT

        def build(self):
            self.parser.add_argument("gistid", action=GistAction)
            self.parser.add_argument("files", nargs='+')
            self.parser.add_argument("-d", "--description", nargs='?', default=None)
            self.parser.set_defaults(func=lambda *args:Edit(*args).invoke())


    class DeleteBuilder(_SimpleBuilder):
        command = DELETE

        def build(self):
            self.parser.add_argument("gistid", action=GistAction)
            self.parser.set_defaults(func=lambda *args:Delete(*args).invoke())


    class RegisterBuilder(_SimpleBuilder):
        command = REGISTER

        def build(self):
            self.parser.add_argument("-u", "--user", nargs='?')
            self.parser.add_argument("-p", "--password", nargs='?')
            self.parser.set_defaults(func=lambda *args:Register(*args).invoke())

