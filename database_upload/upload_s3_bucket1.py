
import botocore
import boto3
from botocore.client import Config

def upload(name):

    ACCESS_KEY_ID = "AKIAZNN5NBT72GR3NKP7"
    ACCESS_SECRET_KEY = "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"
    BUCKET_NAME = "flask121"

    data = open(name, "rb")

    s3 = boto3.resource(
        "s3",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version="s3v4")
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=name, Body=data)

    print("Done")

    #bucket = "flask121"
    #my_bucket = s3.Bucket(bucket)

    my_config = Config(
        signature_version=botocore.UNSIGNED)  # instead of botocore.UNSIGNED use 's3v4' for better url
    s3_client = boto3.client('s3', config=my_config)

    params = {"Bucket": 'flask121', "Key": name}
    url = s3_client.generate_presigned_url('get_object', params, ExpiresIn=3600)
    # print({value: url})

    return {name: url}
