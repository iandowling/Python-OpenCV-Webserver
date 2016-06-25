#!/usr/bin/env python

#python 3 imports
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from flask import Flask, render_template, Response
from camera import Camera
import os
import cv2

#ap name
app = Flask(__name__)

# ssl method
def ssl_wrapper(req):
    @wraps(req)
    def redirect_ssl(*args, **argsv):
        if current_app.config.get("SSL"):
            if request.is_secure:
                return req(*args, **argsv)
            else:
                return redirect(request.url.replace("http://", "https://"))

        return req(*args, **argsv)

    return redirect_ssl

@app.route('/')
def index():
    return render_template('index.html')

# get the camera and pass the frame through the get_frame method in camera.
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# run server method
if __name__ == '__main__':
    app.run('0.0.0.0', debug=False, port=8100, ssl_context=('/home/pi/ssl/server.crt', '/home/pi/ssl/server.key'))