import boto3
from botocore.client import Config

ACCESS_KEY_ID = "AKIAZNN5NBT72JCM2E6M"
ACCESS_SECRET_KEY = "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"
BUCKET_NAME = "flask121"

data = open("baba.jpg", 'rb')

s3 = boto3.resource(
    "s3",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version="s3v4")
)
s3.Bucket(BUCKET_NAME).put_object(Key="baba.jpg", Body=data)

print("Done")
