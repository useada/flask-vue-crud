from flask import Flask, jsonify
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

USERS = [
    {
      "user": "john_doe_1",
      "password": "9X$mK2pL",
      "is_user_admin": False,
      "is_user_manager": True,
      "is_user_tester": False,
      "user_timezone": "America/New_York",
      "is_user_active": True,
      "created_at": "2023-09-15T08:30:45Z"
    },
    {
      "user": "jane_smith_2",
      "password": "7Zt#nR4qJ",
      "is_user_admin": True,
      "is_user_manager": False,
      "is_user_tester": False,
      "user_timezone": "Europe/London",
      "is_user_active": True,
      "created_at": "2023-10-02T14:22:30Z"
    },
    {
      "user": "alex_johnson_3",
      "password": "5Hy$bF8wP",
      "is_user_admin": False,
      "is_user_manager": False,
      "is_user_tester": True,
      "user_timezone": "Asia/Tokyo",
      "is_user_active": True,
      "created_at": "2023-11-20T03:45:12Z"
    },
]

@app.route("/users", methods=["GET"])
def users():
    return jsonify({
        "users": USERS,
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)