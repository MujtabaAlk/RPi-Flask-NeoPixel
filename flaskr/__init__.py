"""
The LedFlask application package.
"""

import os

from flask import Flask, send_from_directory, render_template

from flaskr.ledstrip import LedStrip
from . import db
from . import auth
from . import led


def create_app(test_config=None):
    """
    A factory function that creates the LedFlask app instance.
    :param test_config: The test configuration used when running tests.
    :return: LedFlask app instance.
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when no testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Favicon url
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    # Add database
    db.init_app(app)

    # Register apps
    app.register_blueprint(auth.bp)
    app.register_blueprint(led.bp)

    # Index route
    @app.route("/")
    def index():
        auth.load_logged_in_user()
        led_strip = LedStrip()
        return render_template('led/color.html', color=led_strip.color)

    return app
