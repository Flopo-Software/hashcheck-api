import os
import random
import string

import boto3

from dotenv import load_dotenv

class AwsStorage():
    
    def __init__(self):
        load_dotenv()
        
        self.client = boto3.resource('s3', 
                                        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                                        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                                        region_name=os.getenv("AWS_DEFAULT_REGION"))
        
        self.local_path = os.path.dirname(os.path.abspath(__file__))
        
        self.aws_temp_folder = self.local_path + '/_awstemp'
        
    def upload_file_from_path(self, bucket_name, source_file_name, destination_blob_name):
        bucket = self.get_bucket(bucket_name)
        bucket.upload_file(source_file_name, destination_blob_name)
        
        public_url = self.get_public_url(bucket_name, destination_blob_name)
        
        return public_url
        
    def upload_file_from_memory(self, bucket_name, contents, destination_blob_name):
        bucket = self.get_bucket(bucket_name)
        bucket.put_object(Key=destination_blob_name, Body=contents)
        
        public_url = self.get_public_url(bucket_name, destination_blob_name)
        
        return public_url
    
    def download_file_to_path(self, bucket_name, source_blob_name, destination_file_name):
        bucket = self.get_bucket(bucket_name)
        bucket.download_file(source_blob_name, destination_file_name)
        
        return destination_file_name

    def download_file_into_memory(self, bucket_name, blob_name):
        bucket = self.get_bucket(bucket_name)
    
        temp_filepath = self.generate_temp_path(blob_name)
        
        temp_file = open(temp_filepath, 'wb+')
        bucket.download_fileobj(blob_name, temp_file)
        
        new_file = open(temp_filepath, 'rb')
        string_file = new_file.read()
        
        self.remove_temp_file(temp_filepath)
                            
        return string_file
    
    def get_bucket(self, bucket_name):
        bucket = self.client.Bucket(bucket_name)
        
        return bucket
    
    def get_public_url(self, bucket_name, destination_blob_name):
        object_url = f'https://{bucket_name}.s3.amazonaws.com/{destination_blob_name}'
        
        return object_url
    
    def generate_temp_path(self, blob_name):
        if not (os.path.exists(self.aws_temp_folder)):
            os.mkdir(self.aws_temp_folder)
        
        temp_fileprefix = self.generate_temp_fileprefix()
        temp_filepath = self.aws_temp_folder + '/' + temp_fileprefix + blob_name
        
        return temp_filepath
    
    def generate_temp_fileprefix(self):
        filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        
        return filename
    
    def remove_temp_file(self, temp_filename):
        os.remove(temp_filename)


