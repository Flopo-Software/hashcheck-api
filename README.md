# **API de Upload e Verificação de Documentos no Cloud Storage**

---

## **Descrição do Projeto**

Este projeto é uma API desenvolvida com **Flask** que realiza o upload e a verificação de documentos no Google Cloud Storage. A API calcula o hash dos arquivos recebidos, verifica se eles já existem no bucket e realiza o armazenamento caso sejam inéditos. Se o arquivo já estiver armazenado, a API retorna os metadados do arquivo existente.

---

## **Funcionalidades**

A API possui as seguintes funcionalidades:

1. **Verificação de Arquivos a Partir do Hash**  
   - Recebe um arquivo enviado via `form-data` e calcula o hash.
   - Verifica se o hash do arquivo já existe em um índice local (`hash_index.json`).
   - Caso o arquivo não exista, realiza o upload no bucket do Google Cloud Storage e atualiza o índice.

2. **Upload de Arquivos a Partir da Memória**  
   - Permite o upload de arquivos enviados via `form-data` diretamente para o bucket do Google Cloud Storage.
   - Verifica duplicidade com base no hash antes de realizar o upload.


---

## **Tecnologias Utilizadas**

- **Python**: Linguagem principal da API.
- **Flask**: Framework para desenvolvimento web.
- **Google Cloud Storage**: Serviço de armazenamento de arquivos.
- **pythonCloudStorage**: Abstração personalizada para interagir com o Google Cloud Storage.
- **hashlib**: Biblioteca padrão para cálculo de hashes MD5 e SHA-256.
- **dotenv**: Gerenciamento de variáveis de ambiente a partir de um arquivo `.env`.

---

## **Como Configurar o Projeto**

### **Pré-requisitos**

1. **Python 3.8 ou superior**: Certifique-se de que você possui o Python instalado em sua máquina.
2. **Conta no Google Cloud Platform**:
   - Crie um bucket no Google Cloud Storage.
   - Gere um arquivo de credenciais no formato JSON.
3. **Variáveis de Ambiente**:
   - Configure um arquivo `.env` no diretório raiz do projeto contendo:
     ```plaintext
     GOOGLE_APPLICATION_CREDENTIALS=/caminho/para/seu/perlas-key.json
     BUCKET_NAME=nome_do_bucket
     ```

---

### **Como Executar a API**

1. **Instale as dependências**:
   Execute o seguinte comando para instalar as dependências do projeto:
   ```bash
   pip install -r requirements.txt

2. Configure o ambiente: Certifique-se de que o arquivo .env está configurado corretamente e que o arquivo de credenciais JSON do Google Cloud Storage está no caminho especificado.

3. Inicie o servidor: Execute o servidor Flask:
```bash
python app.py
```
A API estará disponível em http://127.0.0.1:5000.


---

## Endpoints Disponíveis
1. /check-file (POST)
- Descrição: Verifica se um arquivo já existe no bucket com base no hash. Caso não exista, faz o upload do arquivo.
- Requisição:
Enviar um arquivo no formato form-data com a chave file.
- Resposta:
   - 200: Arquivo já existente. Retorna metadados do arquivo.
   - 201: Arquivo enviado com sucesso.
   - 404: Arquivo não encontrado no bucket.
   - 500: Erro interno no servidor.







