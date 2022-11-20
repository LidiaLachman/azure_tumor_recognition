# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:11:33 2022

@author: Lidia
"""

from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024