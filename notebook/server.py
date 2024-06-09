import os
from flask import Flask
from version import get_version

app = Flask(__name__)


@app.get('/')
def home():
    return 'hi there'


if __name__ == '__main__':
    print(f'** Notebook server version: {get_version(os.path.join("notebook", "__init__.py"))}')

    app.run(
        host='0.0.0.0',
        port=5000
    )
