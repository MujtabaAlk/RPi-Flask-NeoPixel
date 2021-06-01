"""
This module is for database related functionalities.
"""
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask import Flask


def get_db():
    """
    Gets the database object associated with the app.
    :return: The database object.
    """
    if 'database' not in g:
        g.database = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.database.row_factory = sqlite3.Row

    return g.database


def close_db(error=None):
    """
    Closes the database object.
    :param error: The error object given by the teardown function.
    """
    database = g.pop('database', None)
    if error is not None:
        print(error)
    if database is not None:
        database.close()


def init_db():
    """
    Clear the existing data and create new tables.
    """
    database = get_db()

    with current_app.open_resource('schema.sql') as file:
        database.executescript(file.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    A command that executes the init_db function and displays a message upon completion.
    """
    init_db()
    click.echo('Initialized the database.')


def init_app(app: Flask):
    """
    Links the database to the Flask app object.
    :param app: The Flask app.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
