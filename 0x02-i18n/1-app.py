"""
Flask App
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    App configurations
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFALUT_TIMEZONE = 'UTC'


# app setup
app = Flask(__name__)
app.url_map.strick_slashes = False
app.config.from_object(Config)

# babel setup
babel = Bable(app)

# routes
@app.route('/')
def index():
    '''Render index page'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
