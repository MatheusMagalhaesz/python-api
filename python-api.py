from flask import Flask, jsonify, request

app = Flask(__name__)

carros = [
    {
        'id': 1,
        'marca': 'Volkswagen',
        'modelo': 'Nivus'
    },
    {
        'id': 2,
        'marca': 'Volkswagen',
        'modelo': 'T-Cross'
    },
    {
        'id': 3,
        'marca': 'Volkswagen',
        'modelo': 'Taos'
    },
    {
        'id': 4,
        'marca': 'Volkswagen',
        'modelo': 'Tiguan'
    }
]


# Consultar (Todos)
@app.route('/carros', methods=['GET'])
def obter_carros():
    return jsonify(carros)


# Consultar (Id)
@app.route('/carros/<int:id>', methods=['GET'])
def obter_carro_com_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)


# Editar
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_por_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carro_alterado)
            return jsonify([indice])


# Criar
@app.route('/carros/<int:id>', methods=['POST'])
def incluir_novo_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro)
    return jsonify(carros)


# Excluir
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carros[indice]
            return jsonify(carros)


app.run(port=5000, host='localhost', debug=True)
