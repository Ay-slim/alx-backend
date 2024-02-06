#!/usr/bin/env python3
"""Module to bootstrap a Flask app with babel"""


from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from typing import Any


app = Flask(__name__)


class Config(object):
    """Babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_locale() -> Any:
    """Fetch a request's locale"""
    req_lang = request.args.get('locale')
    if req_lang and req_lang in app.config['LANGUAGES']:
        return req_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> Any:
    """Application landing page"""
    return render_template('4-index.html',
                           title=gettext('home_title'),
                           body=gettext('home_header'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
