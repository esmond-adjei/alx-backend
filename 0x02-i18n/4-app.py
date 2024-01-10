"""
Flask App
"""
from flask import Flask, render_template, request
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

@babel.localeselector
def get_locale():
    '''configures best match language for user'''
    locale_ = request.args.get('locale')
    if locale_ in app.config['LANGUAGES']:
        return locale_
    return request.accept_languages.best_match(app.config["LANGUAGES"])

# routes
@app.route('/')
def index():
    '''Render index page'''
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
