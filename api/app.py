from urllib.parse import quote as url_quote
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Conexão com o MongoDB
client = MongoClient(os.getenv('MONGO_URI', 'mongodb://mongo:27017/'))
db = client.checklist
tarefas_collection = db.tarefas


@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = list(tarefas_collection.find({}, {'_id': 0}))
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    nova_tarefa = request.json.get('tarefa')
    if nova_tarefa:
        tarefas_collection.insert_one({'tarefa': nova_tarefa})
        return jsonify({'msg': 'Tarefa adicionada com sucesso!'}), 201
    return jsonify({'msg': 'Nenhuma tarefa fornecida!'}), 400


@app.route('/tarefas/<tarefa>', methods=['DELETE'])
def delete_tarefa(tarefa):
    result = tarefas_collection.delete_one({'tarefa': tarefa})
    if result.deleted_count > 0:
        return jsonify({'msg': 'Tarefa excluída com sucesso!'}), 200
    return jsonify({'msg': 'Tarefa não encontrada!'}), 404


if __name__ == '__main__':
    print("Iniciando o servidor Flask...")
    app.run(host='0.0.0.0', port=5000)
