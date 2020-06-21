from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World11112!'


@app.route('/test/')
def test():
    return 'Hello Test111112!'


if __name__ == '__main__':
    app.run()
