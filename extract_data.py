import boto3

bucket = "encrypted-medical-predictions"
# s3 = boto3.resource('s3',
#                     aws_access_key_id='YOUR_ACCESS_KEY',
#                     aws_secret_access_key= 'YOUR_SECRET_KEY')


def download_data(bucket, key, filename):
    downloader = boto3.client('s3' )
    downloader.download_file(bucket, key, filename)


def upload_data(bucket, key, filename):
    downloader = boto3.client('s3')
    downloader.upload_file(filename, bucket, key)
