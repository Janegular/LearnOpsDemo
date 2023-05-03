from imports import *
from constants import *
def create_epic(program_name, title, description, assigned, area_path):
    url = 'https://dev.azure.com/LearnOpsDemo/{}/_apis/wit/workitems/$Epic?api-version=5.1'.format(program_name)

    data = [
    {
        "op": "add",
        "path": "/fields/System.Title",
        "value": title,
        "rel": ""
    },
    {
        "op": "add",
        "path": "/fields/System.AreaPath",
        "value": "{}\{}".format(program_name, area_path),

     },
    {
        "op": "add",
        "path": "/fields/System.Description",
        "value": description,
    },
    {
        "op": "add",
        "path": "/fields/System.AssignedTo",
        "value": assigned,
    }

    ]
    r = requests.post(url, json=data, 
        headers={'Content-Type': 'application/json-patch+json'},
        auth=('', token))
    print(r.status_code)
    print(r.text)
    return r.json()['id']




def create_user_story(program_name, title, description, assigned, area_path):
    url = 'https://dev.azure.com/LearnOpsDemo/{}/_apis/wit/workitems/$User Story?api-version=5.1'.format(program_name)
    data = [
    {
        "op": "add",
        "path": "/fields/System.Title",
        "value": title,
        "rel": ""
    },
    {
        "op": "add",
        "path": "/fields/System.AreaPath",
        "value": "{}\{}".format(program_name, area_path),

     },
    {
        "op": "add",
        "path": "/fields/System.Description",
        "value": description,
    },
    {
        "op": "add",
        "path": "/fields/System.AssignedTo",
        "value": assigned,
    }

    ]
    r = requests.post(url, json=data, 
        headers={'Content-Type': 'application/json-patch+json'},
        auth=('', token))
    print(r.status_code)
    print(r.text)
    return r.json()['id']


def create_task(program_name, title, description, assigned, area_path):
    url = 'https://dev.azure.com/LearnOpsDemo/{}/_apis/wit/workitems/$Task?api-version=5.1'.format(program_name)
    data = [
    {
        "op": "add",
        "path": "/fields/System.Title",
        "value": title,
        "rel": ""
    },
    {
        "op": "add",
        "path": "/fields/System.AreaPath",
        "value": "{}\{}".format(program_name, area_path),

     },
    {
        "op": "add",
        "path": "/fields/System.Description",
        "value": description,
    },
    {
        "op": "add",
        "path": "/fields/System.AssignedTo",
        "value": assigned,
    }

    ]
    r = requests.post(url, json=data, 
        headers={'Content-Type': 'application/json-patch+json'},
        auth=('', token))
    print(r.status_code)
    print(r.text)
    return r.json()['id']
