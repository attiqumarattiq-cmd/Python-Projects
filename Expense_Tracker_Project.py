import json
import csv
from datetime import datetime

DATA_FILE = "expenses.json"
CATEGORIES = ["FOOD", "TRANSPORT", "UTILITIES", "ENTERTAINMENT", "EDUCATION", "OTHER"]

# lOAD THE DATA AT START TO SEE IT AND CHECK IF THERE IS DATA IN IT 

try:
  with open(DATA_FILE, "r") as file:
    app_data = json.load(file)
    if "budget" not in app_data:
        app_data["budget"] = 0.0
    if "expenses" not in app_data:
        app_data["expenses"] = []   
except(FileNotFoundError, json.JSONDecodeError):
    app_data ={"budget": 0.0, "expenses": []}
    
    
#===================================================================

while True:
    print("\n=========== Expense Tracker ==========\n")
    print("1. Add new expense")
    print("2. View data")
    print("3. Budget Capacity")
    print("4. Analyzing the ration on each section")
    print("5. Exporting data to CSV file") 
    print("6. Want to exist the Program")
    print("\n======================================\n")
    
    choice = input("Choose option u want (1-6) :")
    

     
    

        
    
    

