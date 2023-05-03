from imports import *
from constants import *

def find_project(project_name):
    # Connect to the Azure DevOps organization using the Python API
    credentials = BasicAuthentication('', token)
    connection = Connection(org_url, creds=credentials)
    # Get a reference to the Core API client
    core_client = connection.clients.get_core_client()
    get_project_response = core_client.get_projects()
    get_project_list = [get_project_response.value[i].name for i in range(len(get_project_response.value))]
    if project_name in get_project_list:
        print("Project Exists..")
        return True
    else:
        return False



def new_project(project_name, project_description):
    # Connect to the Azure DevOps organization using the Python API
    credentials = BasicAuthentication('', token)
    connection = Connection(org_url, creds=credentials)
    # Get a reference to the Core API client
    core_client = connection.clients.get_core_client()
    capabilities = {
        "versioncontrol": {
                "sourceControlType": "Git"
            },
            "processTemplate": {
                "templateTypeId": "adcc42ab-9882-485e-a3ed-7678f01f66bc"
            }
    }
    project = TeamProject(name=project_name, description=project_description, visibility="enterprise", capabilities=capabilities)
    # Use the Core API client to create the new project
    created_project = core_client.queue_create_project(project)
    print("Project ID:", created_project.id)
    return created_project.id

