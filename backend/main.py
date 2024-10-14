from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def index():
    return ('Hello world')

@app.route("/testItem", methods=["GET"])
def testItem():
    return ('Mensagem Flask')


if __name__ == "__main__":
    app.run(debug=True, port=5000)