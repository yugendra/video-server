
from __future__ import print_function

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import logging
import sys
import time
import pprint
from datetime import datetime

from flask import render_template
from flask import Flask
from flask import send_file
from flask import request

from video import partial_response, get_range

LOG = logging.getLogger(__name__)
app = Flask(__name__)

VIDEO_PATH = '/video'

@app.route('/')
def home():
    LOG.info('Rendering home page')
    response = render_template(
        'index.html',
        video=VIDEO_PATH,
    )
    return response
    
@app.route('/video/<video_name>')
def video(video_name):
    
    path = 'videos/' + video_name

    start, end = get_range(request)
    return partial_response(path, start, end)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    HOST = '0.0.0.0'
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8080)
    IOLoop.instance().start()

    # Standalone
    # app.run(host=HOST, port=8080, debug=True)