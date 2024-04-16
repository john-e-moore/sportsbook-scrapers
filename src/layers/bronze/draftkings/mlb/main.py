import json, yaml, requests
from datetime import datetime
from common.s3_utils import S3Utility

def load_yml(filepath: str) -> dict:
    """Load config from yml file."""
    try:
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(f"Error in configuration file:\n{exc}")

def main():
    # Load config
    config_path = "common/config.yml"
    config = load_yml(config_path)
    bucket = config['aws']['bucket']
    key = config['aws']['bronze_draftkings_s3_key']
    url = config['webscraping']['draftkings']['url']
    sleep_secs = config['webscraping']['draftkings']['sleep']

    # Load API schema
    api_path = "layers/bronze/draftkings/api.yml"
    api = load_yml(api_path)

    # Request data
    # Loop through categories and subcategories
    # Construct url
    # Request then sleeping for 3s
    

    # Write data to s3
    # <subcategory>_<timestamp>.json

if __name__ == '__main__':
    main()