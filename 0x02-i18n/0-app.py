#!/usr/bin/env python3
"""Module to bootstrap a Flask app"""


from flask import Flask, render_template
from typing import Any


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> Any:
    """Application landing page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
