import json
import os

DATABASE_FILE = "my_tasks.json"         # Creates a json file where data will be stored

#======================================================
# STEP 1: SAVING & LOADING
#======================================================

def load_tasks_from_list():
    '''This function reads tasks from JSON file from the hard drive'''
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecoder:
            return []
    return []


def save_tasks_to_disk(tasks_list):
    """Saves Python list to a text file on disk permanently."""
    with open(DATABASE_FILE, "w") as file:
        json.dump(tasks_list, file, indent=4)
    

