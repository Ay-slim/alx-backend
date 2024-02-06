#!/usr/bin/env python3
"""Module to bootstrap a Flask app with babel"""


from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Any


app = Flask(__name__)


class Config(object):
    """Babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localselector
def get_locale() -> Any:
    """Fetch a request's locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> Any:
    """Application landing page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
