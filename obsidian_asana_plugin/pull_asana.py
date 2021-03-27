""" Pulls data from Asana using the API """
import os
import asana
from dotenv import load_dotenv
from log import logger


def connect():
    "Connects to the Asana API"
    # get the api key from .env file
    load_dotenv()
    api_key = os.getenv("ASANA_API_KEY")
    # connect to the api
    client = asana.Client.access_token(api_key)
    return client

def projects(client):
    "Gets a list of projects"
    return client.projects.get_projects(opt_pretty=True)

def main():
    "Executes the main workflow"
    # test the connection to the API
    client = connect()
    print(client)
    # get a list of projects
    print(projects(client))

if __name__ == "__main__":
    main()