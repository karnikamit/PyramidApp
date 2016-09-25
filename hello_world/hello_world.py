# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    # incomin_req = request
    return Response('<body><h1>Hello World!</h1></body>')


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 9000, app)
    server.serve_forever()
