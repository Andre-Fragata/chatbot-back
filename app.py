from flask import Flask, request, jsonify
from context_manager import process_input

app = Flask(__name__)

# Inicializa um dicionário para armazenar contextos de sessões
user_contexts = {}

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json

    # Verifique se a requisição tem os dados esperados
    if 'user_id' not in data or 'message' not in data:
        return jsonify({"error": "Campos 'user_id' e 'message' são obrigatórios."}), 400

    user_id = data['user_id']
    user_message = data['message']

    # Inicialize o contexto do usuário se não existir
    if user_id not in user_contexts:
        user_contexts[user_id] = {"step": 0}

    # Obtenha o contexto atual do usuário
    context = user_contexts[user_id]

    # Processa a entrada do usuário
    response = process_input(user_message, context)

    # Atualiza o contexto do usuário
    user_contexts[user_id] = context

    return jsonify({"response": response, "context": context})

if __name__ == '__main__':
    app.run(debug=True)

