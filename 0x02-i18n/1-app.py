#!/usr/bin/env python3
"""Module to bootstrap a Flask app with babel"""


from flask import Flask, render_template
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


@app.route('/', strict_slashes=False)
def home() -> Any:
    """Application landing page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
