""" Pulls data from Asana using the API """
import os
import json
import requests
import asana
from dotenv import load_dotenv
from log import logger

def connect():
    "Connects to the Asana API"
    # get the api key from .env file
    load_dotenv()
    api_key = os.getenv("ASANA_API_KEY")
    # connect to the api
    headers = {'Authorization': f"Bearer {api_key}"}
    response = requests.get("https://app.asana.com/api/1.0/users/me", headers=headers)
    if response and json.loads(response.text["data"]) is not None:
        logger.info("Connection successful")

if __name__ == "__main__":
    connect()