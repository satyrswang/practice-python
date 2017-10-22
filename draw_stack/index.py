from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Yet another hello!'

if __name__ == '__main__':
    app.run()

