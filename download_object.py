import boto3
import os
from list_objects import list_objects_keys

def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)
    
if __name__ == '__main__':

    bucket = 'jvelazquez-boto3-06202023'
    key = 'test_text_string.txt'
    filename = 'test_text_string.txt'
    
    s3 = boto3.client('s3')

    keys = list_objects_keys(s3, bucket, prefix='folder/')
    
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(s3, bucket, key, key)