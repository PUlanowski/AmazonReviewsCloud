import json
import boto3
import pandas as pd


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    print('Object processed by S3 Object Lambda:')
    rows = s3.get_object(
        Bucket='amazon-reviews-raw-data',
        Key='sample_data.csv')

    df = read.csv(rows['Body'])
    df

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }