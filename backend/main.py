from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)