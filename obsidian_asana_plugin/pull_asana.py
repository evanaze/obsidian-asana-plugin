""" Pulls data from Asana using the API """
import os
import json
import requests
import asana
from dotenv import load_dotenv
from log import logger

def api_call(url):
    "Makes a call to the Asana API given a url"
    headers = {'Authorization': f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    try:
        return json.loads(response.text)
    except Exception:
        raise Exception

def test_connection():
    "Connects to the Asana API"
    # get the api key from .env file
    load_dotenv()
    api_key = os.getenv("ASANA_API_KEY")
    # connect to the api
    url = "https://app.asana.com/api/1.0/users/me"
    response = api_call(url)
    if response["data"] is not None:
        logger.info("API Connection successful")

def projects():
    "Gets a list of projects"
    api_call()

def main():
    "Executes the main workflow"
    # test the connection to the API
    test_connection()
    # get a list of projects


if __name__ == "__main__":
    connect()