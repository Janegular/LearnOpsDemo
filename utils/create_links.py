from imports import *
from constants import * 
def link(parent_id, child_id, program_name):
    url = "https://dev.azure.com/LearnOpsDemo/{}/_apis/wit/workitems/{}?api-version=7.0".format(program_name, child_id)
    data = [
                {
                "op": "add",
                "path": "/relations/-",
                    "value": {
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": "https://dev.azure.com/LearnOpsDemo/{}/_apis/wit/workItems/{}".format(program_name, parent_id),
                    "attributes": {
                        "comment": "Making a new link for the dependency"
                    
                }}}
    ]
    r = requests.patch(url, json=data, 
    headers={'Content-Type': 'application/json-patch+json'},
    auth=('', token))



def create_link(link_array, program_name):
    # link between user story and epics.
    for i in link_array:
       # epic to story link
        us_id = list(link_array[i].keys())
        for us in us_id:
            link(i, us, program_name)
        
        # story to task
    for i in link_array:
        relation_dict = link_array[i]
        for us_id in relation_dict:
            task_list = relation_dict[us_id]
            for task in task_list:
                link(us_id, task, program_name)
