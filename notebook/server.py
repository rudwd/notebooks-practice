from flask import Flask

app = Flask(__name__)


@app.get('/')
def home():
    return 'hi there'


if __name__ == '__main__':
    print(f'** Notebook server starts')

    app.run(
        host='0.0.0.0',
        port=5000
    )
