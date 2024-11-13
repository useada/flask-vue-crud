from flask import Blueprint, jsonify, request
from .models import User
# from . import mongo
from time import time
import pandas as pd
import numpy as np
from .utils import dataframe_to_dict_list

main = Blueprint('main', __name__)

@main.route('/user', methods=['GET', 'POST'])
def user_list():
    if request.method == 'GET':
        # Recupera todos os usuários do MongoDB
        # users = mongo.db.users.find()
        # user_list = [User.from_json(user).to_json() for user in users]
        user_list = []
        return jsonify(user_list), 200

    elif request.method == 'POST':
        # Recebe dados JSON do cliente
        data = request.json
        user = User.from_json(data)

        # Verifica se o username já existe
        # existing_user = mongo.db.users.find_one({'user': user.username})
        # if existing_user:
        #     return jsonify({'error': 'Username already exists.'}), 400

        # Insere no MongoDB
        # mongo.db.users.insert_one(user.to_json())
        return jsonify({'message': 'User added successfully!'}), 201


@main.route('/user/<string:username>', methods=['GET', 'PUT', 'DELETE'])
def user_operations(username):
    if request.method == 'GET':
        # Obtém um usuário específico do MongoDB
        # user_data = mongo.db.users.find_one({'user': username})
        # if user_data:
        #     user = User.from_json(user_data)
        #     return jsonify(user.to_json()), 200
        # else:
        #     return jsonify({'error': 'User not found.'}), 404
        return jsonify({'error': 'User not found.'}), 404

    elif request.method == 'PUT':
        # Recebe dados JSON do cliente
        data = request.json
        # updated_user = User.from_json(data)

        # # Atualiza o campo last_updated_at com o timestamp atual
        # updated_user.last_updated_at = time()

        # # Verifica se o username já existe e não é do mesmo usuário
        # if updated_user.username != username:
        #     existing_user = mongo.db.users.find_one({'user': updated_user.username})
        #     if existing_user:
        #         return jsonify({'error': 'Username already exists.'}), 400

        # # Atualiza o usuário no MongoDB
        # update_data = updated_user.to_json()
        # result = mongo.db.users.update_one({'user': username}, {'$set': update_data})

        # if result.matched_count == 0:
        #     return jsonify({'error': 'User not found.'}), 404

        return jsonify({'message': 'User updated successfully!'}), 200

    elif request.method == 'DELETE':
        # Remove o usuário do MongoDB
        # result = mongo.db.users.delete_one({'user': username})

        # if result.deleted_count == 0:
        #     return jsonify({'error': 'User not found.'}), 404

        return jsonify({'message': 'User deleted successfully!'}), 200



@main.route('/quote/bars', methods=['GET', 'POST'])
def quote_bar():
    if request.method == 'GET':

        df = pd.read_csv("records.csv")

        df['datetime'] = pd.to_datetime(df['date_time'])

        # 将Timestamp对象转换为毫秒时间戳
        df['timestamp'] = df['datetime'].astype(int) // 1e6

        df['open'] = df['price'].shift(1)
        df['close'] = df['price']
        df['volume'] = df['volume'] - df['volume'].shift(1)
        df['turnover'] = df['amount'] - df['amount'].shift(1)
        df['high'] = np.where(df['close'] > df['open'], df['close'], df['open'])
        df['low'] = np.where(df['close'] > df['open'], df['open'], df['close'])

        columns_to_convert = ['timestamp', 'open', 'close', 'high', 'low', 'volume', 'amount', 'buy_open', 'buy_close', 'sell_open', 'sell_close']

        dict_list = dataframe_to_dict_list(df.fillna(0), columns_to_convert)
        
        return jsonify(dict_list), 200


