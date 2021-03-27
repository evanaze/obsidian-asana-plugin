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
    # get the user of the client
    me = client.users.me()
    # find the workspace ID
    projects_workspace = next(workspace for workspace in me['workspaces'] if workspace['name'] == 'Personal')
    # return the results
    return client.projects.find_by_workspace(projects_workspace['gid'], iterator_type=None)

def main():
    "Executes the main workflow"
    # test the connection to the API
    client = connect()
    # get a list of projects
    current_projects = projects(client)

if __name__ == "__main__":
    main()