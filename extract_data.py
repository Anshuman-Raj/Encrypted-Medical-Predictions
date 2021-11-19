import boto3

bucket = "encrypted-medical-predictions"
# s3 = boto3.resource('s3',
#                     aws_access_key_id='YOUR_ACCESS_KEY',
#                     aws_secret_access_key= 'YOUR_SECRET_KEY')


def download_data(bucket, key, filename):
    downloader = boto3.client('s3', aws_access_key_id='AKIA4HBPW4JSZBT3YY4W',
                              aws_secret_access_key='K0PVcjG/nAmTEdY60640c29Rc6L/A9GCJleBXqnq')
    downloader.download_file(bucket, key, filename)


def upload_data(bucket, key, filename):
    downloader = boto3.client('s3', aws_access_key_id='AKIA4HBPW4JSZBT3YY4W',
                              aws_secret_access_key='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')
    downloader.upload_file(filename, bucket, key)
