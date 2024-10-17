from datetime import datetime
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

app.config.from_object(__name__)
app.config["SECRET_KEY"] = "a19cfd19d548617da7e3b47f490b7411db409685"
app.config["MONGO_URI"] = "mongodb+srv://ricardo:ybt26xad@cluster1.pkugvzt.mongodb.net/USERS?retryWrites=true&w=majority&appName=Cluster1"

mongo = PyMongo(app)
db = mongo.db

CORS(app, resources={r"/*": {"origins": "*"}})


# Custom JSON encoder para lidar com ObjectId e datetime
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.isoformat()  # Convertendo datetime para string no formato ISO 8601
        return super(JSONEncoder, self).default(o)

app.json_encoder = JSONEncoder

@app.route("/users", methods=["GET", "POST"])
def users():
  try:
    message = ""
    status = 200
    if request.method == "POST":
      # Receber os dados enviados no corpo da requisição
      user_data = request.get_json()    

      # Adicionar a data de criação automaticamente
      user_data['created_at'] = datetime.utcnow()

      # Inserir os dados no MongoDB
      db.USERS.insert_one(user_data)

      # Retornar uma resposta de sucesso
      message = 'Usuário adicionado com sucesso.'
      status = 201
      # Recuperar todos os documentos da coleção
    data = db.USERS.find()

    # Transformar os dados em uma lista
    result = []
    for doc in data:
      # Remover ou manipular os campos conforme necessário
      user_data = {
        "user": doc.get("user"),
        "password": doc.get("password"),
        "is_user_admin": doc.get("is_user_admin"),
        "is_user_manager": doc.get("is_user_manager"),
        "is_user_tester": doc.get("is_user_tester"),
        "user_timezone": doc.get("user_timezone"),
        "is_user_active": doc.get("is_user_active"),
        "created_at": doc.get("created_at")  # Garantimos que será serializado corretamente
      }
      result.append(user_data)

    # Retornar os dados em formato JSON
    return jsonify({"users": result, "message": message, "status": status})

  except Exception as e:
    return jsonify({"message": str(e)}), 500

#@app.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)