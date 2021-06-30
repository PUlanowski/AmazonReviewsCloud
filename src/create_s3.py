#!/usr/bin/python3
import boto3
import configparser
import logging
import os.path
from botocore.exceptions import ClientError
log = logging.getLogger()


def config_exists():
    if os.path.isfile('C:\\Users\\pit\\Google Drive\\Data Engineering\\Projects\\amazon_reviews\\main.cfg') == True:
        return True
    else:
        log.warning('config file missing')


def config_read():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\pit\\Google Drive\\Data Engineering\\Projects\\amazon_reviews\\main.cfg')
    return config

def s3_client_start():
    config = config_read()

    s3_client = boto3.client(
        's3',
        aws_access_key_id = config['AWS']['ID'],
        aws_secret_access_key = config['AWS']['SECRET'],
        aws_session_token = config['AWS']['TOKEN'],
        region_name = config['AWS']['REGION']
    )
    return s3_client

def create_buckets():
    config = config_read()
    s3_client = s3_client_start()
    bucket_name = [config['S3BUCKET']['NAME_RAW'],config['S3BUCKET']['NAME_FINAL']]

    try:
        bucket_check = s3_client.list_buckets()
        buckets = [bucket['Name'] for bucket in bucket_check['Buckets']]

        for name in bucket_name:
            if (bucket_name in buckets):
                log.warning('Bucket {} already exists'.format(name))
            else:
                s3_client.create_bucket(Bucket = name)
                log.info('Bucket {} created'.format(name))

    except ClientError as e:
        log.error(e)
        return False
    return True

if __name__=="__main__":
    config_exists()
    config_read()
    s3_client_start()
    create_buckets()