from .Gcp import GcpStorage
import os

BUCKET_NAME = os.getenv('BUCKET_NAME', 'pocdetro')  # Default para 'pocdetro'

class CloudStorage():
    def __init__(self, service='gcp'):
        self.accepted_services = {
            'gcp': GcpStorage
        }

        if service not in self.accepted_services:
            raise Exception(f"Serviço inválido: {service} não é suportado")
        
        self.service = self.accepted_services[service]
        self.storage = self.service()
                
    def upload_file_from_path(self, source_file_name, destination_blob_name):
        response = self.storage.upload_file_from_path(
            BUCKET_NAME, 
            source_file_name,
            destination_blob_name
        )        
        return response
        
    def upload_file_from_memory(self, contents, destination_blob_name):
        response = self.storage.upload_file_from_memory(
            BUCKET_NAME, 
            contents,
            destination_blob_name
        )
        return response
    
    def download_file_to_path(self, source_blob_name, destination_file_name):
        response = self.storage.download_file_to_path(
            BUCKET_NAME, 
            source_blob_name,
            destination_file_name
        )
        return response

    def download_file_into_memory(self, blob_name):
        response = self.storage.download_file_into_memory(
            BUCKET_NAME, 
            blob_name
        )
        return response
