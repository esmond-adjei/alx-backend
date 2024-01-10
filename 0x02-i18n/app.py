"""
Flask App
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


# temp db
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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

def get_user():
    '''returns a user for a given id'''
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))

@app.before_request
def before_request():
    '''execute before very request'''
    g.user = get_user(request.args.get('login_as'))

@babel.localeselector
def get_locale():
    '''configures best match language for user'''
    locale_ = request.args.get('locale')
    if locale_ in app.config['LANGUAGES']:
        return locale_
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    locale_ = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return locale_
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    '''configures best match for timezone'''
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


# routes
@app.route('/')
def index():
    '''Render index page'''
    g.time = format_datetime()
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(debug=True)
