import os
import json
from flask import Flask
from version import get_version
from connection import connect_to_db

app = Flask(__name__)

# TODO/NOTE: WARNING - a temporary solution for development.
#   use best practices for persistent database connections with Flask.
connection = connect_to_db()

# TODO: consider using sql alchemy. justify either use case. move to models.py
#  this is for quick poc to verify the feasibility of the schema.
DROP_TABLE = """DROP TABLE IF EXISTS {};"""

CREATE_NOTEBOOK_TABLE = """
        CREATE TABLE notebook (
            notebook_id serial PRIMARY KEY,
            title varchar (150) NOT NULL UNIQUE
        );
        """

CREATE_TYPES = """
        DROP TYPE IF EXISTS step_type;
        CREATE TYPE step_type AS ENUM ('Code', 'Markdown');
"""

CREATE_STEP_TABLE = """
        CREATE TABLE step (
            step_id serial PRIMARY KEY,
            title varchar (150) NOT NULL,
            step_index int,
            type step_type,
            content varchar (255),
            notebook_id int,
            FOREIGN KEY (notebook_id) REFERENCES notebook(notebook_id) ON DELETE CASCADE
        );
"""


@app.get('/')
def home():
    return f'<h2>Notebook exercise by HJ Kim ({get_version()})</h2>'


@app.post('/api/v1/notebooks')
def create_notebook():
    return 'create a new notebook'


@app.get('/api/v1/notebooks')
def get_notebook_by_id():
    return 'get a notebook by ID'


@app.delete('/api/v1/notebooks')
def delete_notebook_by_id():
    return 'delete a notebook by ID'


@app.post('/api/v1/steps')
def create_step():
    return 'create a new step in a notebook'


@app.get('/api/v1/steps')
def get_steps_for_notebook():
    return 'get steps that belong to a notebook'


@app.delete('/api/v1/steps')
def delete_step_in_notebook():
    return 'delete a step by ID that belongs to a notebook'


def init_db(conn, drop_tables: bool = False) -> None:
    """
    Initialises database by creating required tables.
    :param conn: Connection to database
    :param drop_tables: Drop existing tables if true.
    :return: None
    """
    cursor = None
    try:
        cursor = conn.cursor()
        if drop_tables:
            print('WARNING: Dropping existing tables.')
            # TODO: factor out table names
            cursor.execute(DROP_TABLE.format('step'))
            cursor.execute(DROP_TABLE.format('notebook'))

        cursor.execute(CREATE_TYPES)
        cursor.execute(CREATE_NOTEBOOK_TABLE)
        cursor.execute(CREATE_STEP_TABLE)
        conn.commit()
    finally:
        if cursor:
            cursor.close()


if __name__ == '__main__':
    app.config.from_file('config.json', load=json.load)

    print('== Initialise database')
    init_db(connection, drop_tables=app.config["DEV"])

    print(f'** Notebook server version: {get_version(os.path.join("notebook", "__init__.py"))}')
    app.run(
        host=app.config["FLASK_HOST"],
        port=app.config["FLASK_PORT"],
        debug=app.config["DEBUG"]
    )
