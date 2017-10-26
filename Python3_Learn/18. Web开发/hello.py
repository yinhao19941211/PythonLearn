#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=UTF-8')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or '18. Web开发')
    return [body.encode('utf-8')]
