#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gistpy.constant import GITHUB_URL
from restkit import Resource, Connection
from socketpool import ConnectionPool
import json

__all__ = ("Query",)


class Query(object):

    def __init__(self, url=GITHUB_URL, params=None, payload=None, headers=None, filters=None, access_token=None):
        self.url = url
        self.params = params or dict()
        self.payload = payload or dict()
        self.headers = headers or {'Content-Type':'application/json'}
        filters = filters or list()
        self.resource = Resource(
                            url,
                            pool=ConnectionPool(factory=Connection),
                            filters=filters,
                            )
        if access_token is not None:
            self.params["access_token"] = access_token

    def concat_path(self, *args):
        for path in args:
            self.resource.update_uri(path)

    def do_GET(self, path=None, params=None):
        params = params or self.params
        response = self.resource.get(
                                path,
                                self.headers,
                                params)
        return self.parse_response(response.body_string())

    def do_POST(self, path=None, payload=None, params=None):
        payload = payload or self.payload
        params = params or self.params
        response = self.resource.post(
                                path,
                                json.dumps(payload),
                                self.headers,
                                params)
        return self.parse_response(response.body_string())

    def do_DELETE(self, path=None, params=None):
        params = params or self.params
        response = self.resource.delete(
                                path,
                                self.headers,
                                params)
        return self.parse_response(response.body_string())

    def do_PATCH(self, path=None, payload=None, params=None):
        payload = payload or self.payload
        params = params or self.params
        response = self.resource.request(
                                "PATCH",
                                path,
                                json.dumps(payload),
                                self.headers,
                                params)
        return self.parse_response(response.body_string())
    
    def parse_response(self, response):
        try:
            return json.loads(response)
        except:
            return response
    
    def __repr__(self):
        return u"uri:<{0}>".format(self.resource.uri)
    
    def __str__(self):
        return self.resource.uri

