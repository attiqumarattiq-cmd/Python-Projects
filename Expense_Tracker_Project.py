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
    

        
    
    

