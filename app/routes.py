import hashlib
import json
import os
from flask import Blueprint, request, jsonify
from google.cloud import storage  
from app.utils import hash_index, save_hash_index 
from dotenv import load_dotenv
load_dotenv()


bp = Blueprint('routes', __name__)

GCS_BUCKET_NAME = "pocdetro" 

@bp.route('/check-file', methods=['POST'])
def check_file_existence():
    file = request.files.get('file')  # Arquivo enviado via form-data

    if not file:
        return jsonify({"error": "Arquivo é obrigatório"}), 400

    try:
        file.seek(0)
        file_hash = hashlib.md5(file.read()).hexdigest()
        file.seek(0)

        if file_hash in hash_index:
            return jsonify({
                "message": "Arquivo já existe no bucket",
                "hash": file_hash,
                "file_name": hash_index[file_hash]
            }), 200


        client = storage.Client()
        bucket = client.bucket(GCS_BUCKET_NAME)
        blob = bucket.blob(file.filename)

        file.seek(0)  
        blob.upload_from_file(file)

        hash_index[file_hash] = file.filename
        save_hash_index(hash_index) 

        return jsonify({
            "message": "Arquivo não encontrado no bucket, mas foi enviado",
            "hash": file_hash,
            "file_name": file.filename
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
