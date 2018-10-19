#!/usr/bin/env python

"""Define server logic and endpoints for our web app."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
from flask import Flask, request, Response


application = Flask(__name__)


@application.route('/names/', methods=['POST'])
def handle_request():
    """Define server logic for 'name' endpoint."""
    if request.json is None:
        return Response("", status=415)

    if 'name' not in request.json.keys():
        return Response("Missing name", status=400)

    try:
        name = request.json['name']
        output = "Hello, %s!" % name.title()
        return Response(output, status=200)
    except Exception as ex:
        logging.exception('Error processing message: %s' % request.json)
        return Response(ex.message, status=500)


if __name__ == '__main__':
    application.run(debug=True)
