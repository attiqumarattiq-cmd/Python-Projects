import json
import os

DATABASE_FILE = "my_tasks.json"         # Creates a json file where data will be stored

#======================================================
# STEP 1: SAVING & LOADING
#======================================================

def load_tasks_from_list():
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecoder:
            return []
    return []

