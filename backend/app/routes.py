from flask import Blueprint, jsonify, request
from .models import User
from . import mongo

main = Blueprint('main', __name__)

@main.route('/user', methods=['GET', 'POST'])
def user_list():
    if request.method == 'GET':
        # Recupera todos os usuários do MongoDB
        users = mongo.db.users.find()
        user_list = [User.from_json(user).to_json() for user in users]
        return jsonify(user_list), 200

    elif request.method == 'POST':
        # Recebe dados JSON do cliente
        data = request.json
        user = User.from_json(data)

        # Verifica se o username já existe
        existing_user = mongo.db.users.find_one({'user': user.username})
        if existing_user:
            return jsonify({'error': 'Username already exists.'}), 400

        # Insere no MongoDB
        mongo.db.users.insert_one(user.to_json())
        return jsonify({'message': 'User added successfully!'}), 201


@main.route('/user/<string:username>', methods=['GET', 'PUT', 'DELETE'])
def user_operations(username):
    if request.method == 'GET':
        # Obtém um usuário específico do MongoDB
        user_data = mongo.db.users.find_one({'user': username})
        if user_data:
            user = User.from_json(user_data)
            return jsonify(user.to_json()), 200
        else:
            return jsonify({'error': 'User not found.'}), 404

    elif request.method == 'PUT':
        # Recebe dados JSON do cliente
        data = request.json
        updated_user = User.from_json(data)

        # Verifica se o username já existe e não é do mesmo usuário
        if updated_user.username != username:
            existing_user = mongo.db.users.find_one({'user': updated_user.username})
            if existing_user:
                return jsonify({'error': 'Username already exists.'}), 400

        # Atualiza o usuário no MongoDB
        update_data = updated_user.to_json()
        result = mongo.db.users.update_one({'user': username}, {'$set': update_data})

        if result.matched_count == 0:
            return jsonify({'error': 'User not found.'}), 404

        return jsonify({'message': 'User updated successfully!'}), 200

    elif request.method == 'DELETE':
        # Remove o usuário do MongoDB
        result = mongo.db.users.delete_one({'user': username})

        if result.deleted_count == 0:
            return jsonify({'error': 'User not found.'}), 404

        return jsonify({'message': 'User deleted successfully!'}), 200

