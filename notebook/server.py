import os
import json
from flask import Flask
from version import get_version
from connection import connect_to_db

app = Flask(__name__)

# TODO/NOTE: WARNING - a temporary hack for development due to time limit.
#   search and refer to solutions for "best practices for persistent database connections with Flask..."
connection = connect_to_db()


@app.get('/')
def home():
    return 'hi there'


if __name__ == '__main__':
    app.config.from_file('config.json', load=json.load)

    print(f'** Notebook server version: {get_version(os.path.join("notebook", "__init__.py"))}')
    app.run(
        host=app.config["FLASK_HOST"],
        port=app.config["FLASK_PORT"],
        debug=app.config["DEBUG"]
    )
