import hashlib
import json
import os
from flask import Blueprint, request, jsonify
from google.cloud import storage  # Biblioteca para GCS
from app.utils import hash_index, save_hash_index  # Função para salvar o índice
from dotenv import load_dotenv
load_dotenv()


bp = Blueprint('routes', __name__)

# Configuração para o Google Cloud Storage
GCS_BUCKET_NAME = "pocdetro"  # Substitua pelo nome do seu bucket

@bp.route('/check-file', methods=['POST'])
def check_file_existence():
    file = request.files.get('file')  # Arquivo enviado via form-data

    if not file:
        return jsonify({"error": "Arquivo é obrigatório"}), 400

    try:
        # Calcular o hash do arquivo recebido
        file.seek(0)
        file_hash = hashlib.md5(file.read()).hexdigest()
        file.seek(0)

        # Verificar no índice de hashes
        if file_hash in hash_index:
            return jsonify({
                "message": "Arquivo já existe no bucket",
                "hash": file_hash,
                "file_name": hash_index[file_hash]
            }), 200

        # Caso o arquivo não seja encontrado no índice
        # Fazer upload para o Google Cloud Storage
        client = storage.Client()
        bucket = client.bucket(GCS_BUCKET_NAME)
        blob = bucket.blob(file.filename)

        file.seek(0)  # Certifique-se de reposicionar o cursor
        blob.upload_from_file(file)

        # Adicionar o novo hash ao índice
        hash_index[file_hash] = file.filename
        save_hash_index(hash_index)  # Salvar o índice atualizado no disco

        return jsonify({
            "message": "Arquivo não encontrado no bucket, mas foi enviado",
            "hash": file_hash,
            "file_name": file.filename
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
