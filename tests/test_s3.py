from src.create_s3 import config_exists

#check if config exists
def test_config_exists():
    assert config_exists() == True
