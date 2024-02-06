#!/usr/bin/env python3
"""1-app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config object for babel"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns the default locale"""
    request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """renders templates/2-index.html"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)