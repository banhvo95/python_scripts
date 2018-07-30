from flask import Flask

#app is flask object
#pass in name to help Flask determine root path
app = Flask(__name__)


@app.route("/")
@app.route("/home/")
def home():
    return "<h1>Homepage</h1>"

@app.route("/about/")
def hello1():
    return "Hello Nerds"


if __name__ == '__main__':
    app.run(debug=True)