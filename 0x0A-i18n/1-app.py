#!/usr/bin/env python3
""" Route module for the API """
from flask import Flask, request, render_template
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
app.config.from_object('Config')


class Config(object):
    """ Babel configuration """
    LANGUAGES = ['en', 'fr']
    # these are the inherent defaults
    BABEL_DEFAULT_LOCALE = ['en']
    BABEL_DEFAULT_TIMEZONE = ['UTC']


babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 1-index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
