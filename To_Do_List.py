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
        


#=====================================================================
#------------ MAIN CONTROL PANEL --------------
#=====================================================================

def main():
    
    tasks_database = load_tasks_from_disk()
    print(tasks_database)

    while True:
        print("\n=== TO DO LIST ENGINE ===")
        print("1. View all tasks.")
        print("2. Add a new task.")
        print("3. Delete a task")
        print("4. Exist Program")


