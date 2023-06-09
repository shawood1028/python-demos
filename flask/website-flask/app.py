from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api")
def hello_api():
    return "<p>Hello, Api!</p>"

if __name__ == '__main__':
    app.run()