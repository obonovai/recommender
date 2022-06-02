#!/usr/bin/env python3

# Written by Ivona Obonova
# 22.2.2022

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    from .controller import controller
    app.register_blueprint(controller, url_prefix='/')

    from .knn import Knn
    Knn.init()

    return app
