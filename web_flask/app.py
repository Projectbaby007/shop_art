#!/usr/bin/python3
"""
This module defines a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_shopart():
    """Display ‘Hello Shopart!’”””
    return 'Hello Shopart!’


if __name__ == '__main__':
    app.run(host='0.0.0.0’, port=5000)

