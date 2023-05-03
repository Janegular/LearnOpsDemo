from imports import *
from constants import *

def find_area_path(project_name, domain):
    urls = "https://dev.azure.com/LearnOpsDemo/{}/_apis/wit/classificationnodes/Areas/{}?api-version=7.0".format(project_name, domain)
    r = requests.get(urls, 
        auth=('', token))
    if r.status_code == 200:
        print("Area path exists")
        return True
    elif r.status_code == 404:
        print("Area path does not exist")
        return False

def create_area_path(project_name, domain):
    url = "https://dev.azure.com/LearnOpsDemo/{}/_apis/wit/classificationnodes/Areas?api-version=7.0".format(project_name)

    data =  {
        "name": domain,
        }

    r = requests.post(url, json=data, 
        # headers={'Content-Type': 'application/json-patch+json'},
        auth=('', token))
    if r.status_code == 201:
        return True
    else: 
        return False