import os
import json

HASH_INDEX_FILE = "/Users/joaovitormallet/Documents/IC/FLopoAnonimizacao/hashcheck-api/hash_index.json"

def load_hash_index():
    if os.path.exists(HASH_INDEX_FILE):
        with open(HASH_INDEX_FILE, 'r') as f:
            return json.load(f)
    else:
        print(f"Arquivo {HASH_INDEX_FILE} não encontrado. Inicializando índice vazio.")
        return {}

def save_hash_index(hash_index):
    with open(HASH_INDEX_FILE, 'w') as f:
        json.dump(hash_index, f, indent=4)
        print(f"Índice de hashes atualizado em {HASH_INDEX_FILE}")

hash_index = load_hash_index()
