import json
import csv
from datetime import datetime

# ==========================================
# 1. INITIAL SETUP & PERSISTENCE LOAD
# ==========================================
DATA_FILE = "expenses.json"
CATEGORIES = ["Food", "Transport", "Utilities", "Entertainment", "Education", "Other"]

# Load the data straight from the file at startup without using custom functions
try:
    with open(DATA_FILE, "r") as file:
        app_data = json.load(file)
        if "budget" not in app_data:
            app_data["budget"] = 0.0
        if "expenses" not in app_data:
            app_data["expenses"] = []
except (FileNotFoundError, json.JSONDecodeError):
    app_data = {"budget": 0.0, "expenses": []}

# ==========================================
# 2. MAIN INTERACTIVE APPLICATION LOOP
# ==========================================
while True:
    print("\n" + "="*50)
    print("    🛡️ DECODELABS ENTERPRISE EXPENSE TRACKER 🛡️")
    print("="*50)
    print(" 1. Add New Expense Record")
    print(" 2. View Historical Log Data")
    print(" 3. Configure Budget Capacity Threshold")
    print(" 4. Analyze Categorized Spending Ratios")
    print(" 5. Export Analytical Log to Spreadsheet CSV")
    print(" 6. Exit Application Environment")
    print("="*50)
    
    choice = input("Select operation pipeline (1-6): ").strip()
    
    # ------------------------------------------
    # PIPELINE 1: ADD NEW EXPENSE RECORD
    # ------------------------------------------
    if choice == "1":
        print("\n--- Add New Expense Record ---")
        
        # Validate Amount Input
        while True:
            try:
                amount_str = input("Enter amount (PKR): ").strip()
                expense_amount = float(amount_str)
                if expense_amount <= 0:
                    print("❌ Error: Amount must be greater than zero.")
                    continue
                expense_amount = round(expense_amount, 2)
                break
            except ValueError:
                print("❌ Error: Invalid format. Enter a valid decimal or integer.")
        
        # Validate Category Selection
        print("\nAvailable Categories:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"  {i}. {cat}")
        
        while True:
            cat_choice = input(f"Select category (1-{len(CATEGORIES)}): ").strip()
            try:
                idx = int(cat_choice) - 1
                if 0 <= idx < len(CATEGORIES):
                    expense_category = CATEGORIES[idx]
                    break
            except ValueError:
                pass
            
            capitalized = cat_choice.capitalize()
            if capitalized in CATEGORIES:
                expense_category = capitalized
                break
            print("❌ Error: Please select a valid number or type a category from the list.")
        
        # Validate Date Input
        while True:
            date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date_str:
                expense_date = datetime.today().strftime('%Y-%m-%d')
                break
            try:
                valid_date = datetime.strptime(date_str, '%Y-%m-%d')
                expense_date = valid_date.strftime('%Y-%m-%d')
                break
            except ValueError:
                print("❌ Error: Date format must be exactly YYYY-MM-DD.")
        
        # Fetch Description
        expense_desc = input("Enter a brief description: ").strip()
        if not expense_desc:
            expense_desc = "No description provided."
            
        # Structure the Multi-Dimensional Dictionary
        record = {
            "date": expense_date,
            "amount": expense_amount,
            "category": expense_category,
            "description": expense_desc
        }
        
        # Update Dataset and Save Directly to File
        app_data["expenses"].append(record)
        with open(DATA_FILE, "w") as file:
            json.dump(app_data, file, indent=4)
            
        print("✅ Expense added successfully!")
        
        # Immediate Budget Status Check
        if app_data["budget"] > 0.0:
            total_spent = sum(item["amount"] for item in app_data["expenses"])
            print(f"📊 Budget Status: Spent PKR {total_spent:,.2f} out of your PKR {app_data['budget']:,.2f} cap limit.")
            if total_spent > app_data["budget"]:
                print(f"🚨 ALERT: You have breached your configured budget threshold by PKR {total_spent - app_data['budget']:,.2f}!")
            elif total_spent >= (app_data["budget"] * 0.9):
                print("⚠️ WARNING: You have utilized over 90% of your allocated monthly budget allowance.")

    # ------------------------------------------
    # PIPELINE 2: VIEW HISTORICAL LOG DATA
    # ------------------------------------------
    elif choice == "2":
        expenses = app_data["expenses"]
        if not expenses:
            print("\n⚠️ No expense data found. Record some expenses first!")
            continue

        print("\n================================== EXPENSE LOG HISTORICAL REPORT ==================================")
        print(f"{'Index':<6} | {'Date':<12} | {'Category':<15} | {'Amount (PKR)':<15} | {'Description'}")
        print("-" * 100)
        
        total_sum = 0.0
        for idx, exp in enumerate(expenses, 1):
            print(f"{idx:<6} | {exp['date']:<12} | {exp['category']:<15} | {exp['amount']:<15,.2f} | {exp['description']}")
            total_sum += exp["amount"]
            
        print("-" * 100)
        print(f"{'TOTAL EXPENSES METRIC':<39} | {total_sum:<15,.2f} |")
        print("====================================================================================================")

    # ------------------------------------------
    # PIPELINE 3: CONFIGURE BUDGET THRESHOLD
    # ------------------------------------------
    elif choice == "3":
        print("\n--- Configure Financial Budget Cap ---")
        while True:
            try:
                budget_str = input("Enter your monthly budget cap target (PKR): ").strip()
                budget_val = float(budget_str)
                if budget_val < 0:
                    print("❌ Error: Budget cannot be negative.")
                    continue
                app_data["budget"] = round(budget_val, 2)
                
                with open(DATA_FILE, "w") as file:
                    json.dump(app_data, file, indent=4)
                    
                print(f"✅ Budget cap updated successfully to: PKR {app_data['budget']:,}")
                break
            except ValueError:
                print("❌ Error: Invalid number entry.")

    # ------------------------------------------
    # PIPELINE 4: ANALYZE CATEGORIZED SPENDING
    # ------------------------------------------
    elif choice == "4":
        expenses = app_data["expenses"]
        if not expenses:
            print("\n⚠️ Analytics cannot execute without structural dataset patterns.")
            continue

        total_spent = sum(item["amount"] for item in expenses)
        category_totals = {cat: 0.0 for cat in CATEGORIES}
        
        for exp in expenses:
            cat = exp["category"]
            if cat in category_totals:
                category_totals[cat] += exp["amount"]
            else:
                category_totals["Other"] += exp["amount"]

        print("\n====================== CATEGORY BREAKDOWN METRICS ======================")
        print(f"{'Category Label':<18} | {'Total Spending (PKR)':<22} | {'Percentage Breakdown'}")
        print("-" * 65)
        
        for cat, amt in category_totals.items():
            percentage = (amt / total_spent * 100) if total_spent > 0 else 0.0
            bar = "█" * int(percentage // 5)
            print(f"{cat:<18} | {amt:<22:,.2f} | {percentage:<5.1f}% {bar}")
            
        print("-" * 65)
        print(f"{'AGGREGATE TOTAL':<18} | {total_spent:<22:,.2f} | 100.0%")
        print("=========================================================================")

    # ------------------------------------------
    # PIPELINE 5: EXPORT TO CSV SPREADSHEET
    # ------------------------------------------
    elif choice == "5":
        expenses = app_data["expenses"]
        if not expenses:
            print("\n⚠️ No dataset available to extract CSV compilation records.")
            continue
        
        filename = "exported_expenses.csv"
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Category", "Amount (PKR)", "Description"])
                for exp in expenses:
                    writer.writerow([exp['date'], exp['category'], exp['amount'], exp['description']])
            print(f"✅ Production dataset exported cleanly into local runtime directory: '{filename}'")
        except IOError:
            print("❌ Error: Local file operations permission conflict prevented write tasks.")

    # ------------------------------------------
    # PIPELINE 6: EXIT APPLICATION ENVIRONMENT
    # ------------------------------------------
    elif choice == "6":
        print("\n💾 Terminating execution environment. Database modifications synchronized safely. Goodbye!")
        break
        
    else:
        print("❌ Error: Instruction payload not mapped to active options. Enter a number from 1 to 6.")
