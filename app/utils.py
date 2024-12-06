import os
import json

# Caminho para o índice de hashes
HASH_INDEX_FILE = "/Users/joaovitormallet/Documents/IC/FLopoAnonimizacao/hashcheck-api/hash_index.json"

# Função para carregar o índice de hashes do arquivo JSON
def load_hash_index():
    if os.path.exists(HASH_INDEX_FILE):
        with open(HASH_INDEX_FILE, 'r') as f:
            return json.load(f)
    else:
        print(f"Arquivo {HASH_INDEX_FILE} não encontrado. Inicializando índice vazio.")
        return {}

# Função para salvar o índice de hashes no arquivo JSON
def save_hash_index(hash_index):
    with open(HASH_INDEX_FILE, 'w') as f:
        json.dump(hash_index, f, indent=4)
        print(f"Índice de hashes atualizado em {HASH_INDEX_FILE}")

# Inicializar o índice de hashes
hash_index = load_hash_index()
