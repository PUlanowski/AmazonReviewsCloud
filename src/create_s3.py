#!/usr/bin/python3
import boto3
import configparser
import logging
import os.path
from botocore.exceptions import ClientError
logging = logging.getLogger().setLevel(logging.INFO)

def config_exists():
    if os.path.isfile('main.cfg') == True:
        return True