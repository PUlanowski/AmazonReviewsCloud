from src.create_s3 import config_exists
from src.create_s3 import config_read
from src.create_s3 import s3_client_start


#check if config exists
def test_config_exists():
    """
    GIVEN creating S3 bucket process starts
    WHEN try to fetch credentials
    THEN file with credentials exists
    """
    assert (config_exists() == True), 'config file not present in project'

def test_config_read():
    """
    GIVEN configuration file exists
    WHEN config is read
    THEN all values are available for further usage
    """
    config = config_read()
    assert (config['AWS']['REGION'] == 'us-east-1'), "config value for AWS REGION is incorrect"

def test_s3_client_start():
    """
    GIVEN configuration file is available
    WHEN creating boto3 session for S3
    THEN function is returning s3 client cursor
    """
    s3_client = s3_client_start()
    assert s3_client is not None