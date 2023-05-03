"""
Master notebook that takes care of the execution
"""
# Importing the required packages and modules
from utils.create_new_project import *
from utils.create_area_path import *
from utils.create_work_items import *
from utils.create_links import *

def entry(program_name, project_description, domain, skills):
    # find project
    status = find_project(program_name)
    # create a new project
    if not status:
        project_id = new_project(program_name, project_description)
    # finding an area path
    status = find_area_path(program_name, domain)
    if not status: 
        # creating an area path
        status = create_area_path(program_name, domain)
    # creating user story and tasks and epics
    link_array = dict()
    for title in skills:
        epic_id = create_epic(program_name, title, "", resource_name, domain)
        link_array[epic_id] = list()
        df = pd.read_csv("data/{}.csv".format(title))
        relation_dict = dict()
        for index, row in df.iterrows():
                us_id = create_user_story(program_name, row["User Story Title"], row["User Story Description"], resource_name, domain)
                relation_dict[us_id] = []
                tasks = json.loads(row["Task"])
                print(len(tasks))
                for task in tasks:
                        t_id = create_task(program_name, task['title'], task["description"], resource_name, domain)
                        relation_dict[us_id].append(t_id)
                link_array[epic_id] = relation_dict
    create_link(link_array, program_name)

if __name__ == "__main__":
    resource_name = "Hariprasad Bobbala"
    program_name = "Hari_UpSkill"
    domain = "ACAI" # Can be acai, BZ , MW
    skills = ["AzureFunctions", "csharp"]
    entry(program_name, "This is a demo project", domain, skills)