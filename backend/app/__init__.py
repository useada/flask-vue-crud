from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Configuração do MongoDB
    app.config["MONGO_URI"] = Config.MONGO_URI
    mongo.init_app(app)

    # Importa e registra as rotas
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
