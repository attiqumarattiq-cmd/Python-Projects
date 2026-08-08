import json
import os

DATABASE_FILE = "my_tasks.json"         # Creates a json file where data will be stored

#======================================================
# STEP 1: SAVING & LOADING
#======================================================

def load_tasks_from_disk():
    #'''Reads tasks from a json file on your hard drive'''
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecoderError:
            return[]
        return[]
    
    
def save_tasks_to_disk(tasks_list):
    with open(DATABASE_FILE, "w") as file:
        json.dump(tasks_list, file, index = 4)  
        # converts python data to json data formate
        #tasks_list: The first argument; the Python data structure you are saving.file: 
        #The second argument:  The target file object where the data is being written
        





