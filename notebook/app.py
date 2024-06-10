import os
import json
from flask import Flask
from version import get_version
from connection import connect_to_db

app = Flask(__name__)

# TODO/NOTE: WARNING - a temporary solution for development.
#   refer to "best practices for persistent database connections with Flask
connection = connect_to_db()

# TODO: consider using sql alchemy. justify either use case.
#  this is for quick poc to verify the feasibility of the schema.
DROP_TABLE = """DROP TABLE IF EXISTS {};"""

CREATE_NOTEBOOK_TABLE = """
        CREATE TABLE notebook (
            notebook_id serial PRIMARY KEY,
            title varchar (150) NOT NULL UNIQUE
        );
        """

CREATE_STEP_TABLE = """
        CREATE TYPE step_type AS ENUM ('Code', 'Markdown');

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
    return {
        'greeting': 'hi there'
    }


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
