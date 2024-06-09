import os
import json
from flask import Flask
from version import get_version

app = Flask(__name__)


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
