# **API de Upload e Verificação de Documentos no Cloud Storage**
---

## **Descrição do Projeto**

Este projeto é uma API desenvolvida com **Flask** que realiza o upload e a verificação de documentos no Google Cloud Storage. A API calcula o hash dos arquivos recebidos, verifica se eles já existem no bucket e realiza o armazenamento caso sejam inéditos. Se o arquivo já estiver armazenado, a API retorna os metadados do arquivo existente.

---

## **Funcionalidades**

A API possui as seguintes funcionalidades:

1. **Upload de Arquivos a Partir da Memória**  
   Permite o upload de arquivos enviados via `form-data` para o bucket. O hash do arquivo é calculado para evitar duplicação.

2. **Upload de Arquivos a Partir do Disco**  
   Realiza o upload de arquivos que já estão salvos no servidor, verificando duplicidade com base no hash.

3. **Download de Arquivos do Bucket para o Disco**  
   Permite baixar arquivos do bucket e salvá-los em um local no sistema de arquivos.

4. **Download de Arquivos do Bucket para a Memória**  
   Faz o download de arquivos diretamente para a memória, sem salvá-los no disco.

---

## **Tecnologias Utilizadas**

- **Python**: Linguagem principal da API.
- **Flask**: Framework para desenvolvimento web.
- **Google Cloud Storage**: Serviço de armazenamento de arquivos.
- **pythonCloudStorage**: Abstração para interagir com o Google Cloud Storage.
- **hashlib**: Biblioteca padrão para cálculo de hashes MD5 e SHA-256.

---

## **Como Configurar o Projeto**

### **Pré-requisitos**

1. Python 3.8 ou superior.
2. Conta no Google Cloud Platform com um bucket configurado.
3. Variável de ambiente `BUCKET_NAME` com o nome do bucket no Google Cloud Storage.
4. Configuração de autenticação com o Google Cloud:
   - Um arquivo de credenciais JSON deve ser configurado no ambiente como `GOOGLE_APPLICATION_CREDENTIALS`.


### Como Executar a API
---

1. Certifique-se de que as variáveis de ambiente estão configuradas corretamente.
2. Execute o servidor Flask:
`flask run`
3. A API estará disponível em http://127.0.0.1:5000.


### Endpoints da API







