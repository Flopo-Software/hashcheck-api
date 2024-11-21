import os
import hashlib
from flask import Blueprint, request, jsonify
from pythonCloudStorage.Storage import CloudStorage


# Definir o nome do bucket diretamente ou buscar da variável de ambiente
BUCKET_NAME = os.getenv('BUCKET_NAME', 'pocdetro')

bp = Blueprint('routes', __name__)
cloud_storage = CloudStorage(service='gcp')

@bp.route('/upload/memory', methods=['POST'])
def upload_file_from_memory():
    file = request.files.get('file')  # Arquivo enviado via form-data
    destination_blob_name = request.form.get('destination_blob_name')  # Nome no bucket

    if not file or not destination_blob_name:
        return jsonify({"error": "Arquivo e destination_blob_name são obrigatórios"}), 400

    try:
        # Calcular o hash do arquivo
        file.seek(0)  # Garante que estamos no início do arquivo
        file_hash = hashlib.md5(file.read()).hexdigest()
        file.seek(0)  # Reseta o ponteiro do arquivo para reutilizá-lo

        # Verificar se o arquivo já existe no bucket usando o hash como identificador
        hash_blob_name = f"{file_hash}_{destination_blob_name}"
        bucket = cloud_storage.storage.storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(hash_blob_name)

        if blob.exists():
            return jsonify({
                "message": "Arquivo já existe no bucket",
                "hash": file_hash,
                "file_url": blob.public_url
            }), 200

        # Caso o arquivo não exista, realizar o upload com o hash no nome
        public_url = cloud_storage.upload_file_from_memory(
            BUCKET_NAME,
            file,
            hash_blob_name
        )

        return jsonify({
            "message": "Upload realizado com sucesso",
            "hash": file_hash,
            "file_url": public_url
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/upload/path', methods=['POST'])
def upload_file_from_path():
    source_file_name = request.json.get('source_file_name')  # Caminho local do arquivo
    destination_blob_name = request.json.get('destination_blob_name')  # Nome no bucket

    if not source_file_name or not destination_blob_name:
        return jsonify({"error": "source_file_name e destination_blob_name são obrigatórios"}), 400

    try:
        # Calcular o hash do arquivo
        with open(source_file_name, "rb") as file:
            file_hash = hashlib.md5(file.read()).hexdigest()

        # Verificar se o arquivo já existe no bucket usando o hash como identificador
        hash_blob_name = f"{file_hash}_{destination_blob_name}"
        bucket = cloud_storage.storage.storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(hash_blob_name)

        if blob.exists():
            return jsonify({
                "message": "Arquivo já existe no bucket",
                "hash": file_hash,
                "file_url": blob.public_url
            }), 200

        # Caso o arquivo não exista, realizar o upload com o hash no nome
        public_url = cloud_storage.upload_file_from_path(
            BUCKET_NAME,
            source_file_name,
            hash_blob_name
        )

        return jsonify({
            "message": "Upload realizado com sucesso",
            "hash": file_hash,
            "file_url": public_url
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/download/path', methods=['POST'])
def download_file_to_path():
    source_blob_name = request.json.get('source_blob_name')  # Nome do arquivo no bucket
    destination_file_name = request.json.get('destination_file_name')  # Caminho local para salvar

    if not source_blob_name or not destination_file_name:
        return jsonify({"error": "source_blob_name e destination_file_name são obrigatórios"}), 400

    try:
        # Baixar o arquivo do bucket para o disco local
        local_file = cloud_storage.download_file_to_path(source_blob_name, destination_file_name)
        return jsonify({"message": "Download realizado com sucesso", "local_file": local_file}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/download/memory', methods=['POST'])
def download_file_into_memory():
    blob_name = request.json.get('blob_name')  # Nome do arquivo no bucket

    if not blob_name:
        return jsonify({"error": "blob_name é obrigatório"}), 400

    try:
        # Baixar o arquivo para a memória
        contents = cloud_storage.download_file_into_memory(blob_name)
        return jsonify({
            "message": "Download realizado com sucesso",
            "contents": contents.decode('utf-8')
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
