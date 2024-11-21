from dotenv import load_dotenv
from google.cloud import storage

class GcpStorage():
    def __init__(self):
        # Carregar as variáveis de ambiente do .env
        load_dotenv()
        self.storage_client = storage.Client()

    def upload_file_from_path(self, bucket_name, source_file_name, destination_blob_name):
        blob = self.create_blob(bucket_name, destination_blob_name)
        blob.upload_from_filename(source_file_name)
        return blob.public_url
        
    def upload_file_from_memory(self, bucket_name, contents, destination_blob_name):
        blob = self.create_blob(bucket_name, destination_blob_name)
        blob.upload_from_file(contents)
        return blob.public_url
    
    def download_file_to_path(self, bucket_name, source_blob_name, destination_file_name):
        blob = self.create_blob(bucket_name, source_blob_name)
        blob.download_to_filename(destination_file_name)
        return destination_file_name

    def download_file_into_memory(self, bucket_name, blob_name):
        blob = self.create_blob(bucket_name, blob_name)
        contents = blob.download_as_string()
        return contents

    def create_blob(self, bucket_name, content):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(content)
        return blob
