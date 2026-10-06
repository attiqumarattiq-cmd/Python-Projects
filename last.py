
def calculate_discount():
    bill_amount = int(input("Enter bill amount: "))

    if bill_amount >= 5000:
        print("Discount applied: 20%")
        bill_amount = bill_amount - (20 / 100)*bill_amount
    elif bill_amount >= 2000:
        print("Discount applied: 10%")
        bill_amount = bill_amount - (10 / 100)*bill_amount
    elif bill_amount >= 1000:
        print("Discount applied: 5%")
        bill_amount = bill_amount - (5 / 100)*bill_amount
    elif bill_amount < 1000:
        print("Discount applied: No Discount")
    print("=================================================================")
        
        
        
    
def check_membership():
    print("=========================================")
    tier = input("Enter membership tier: ")
    purchase_amount = int(input("Enter purchase amount: "))
    print("=========================================")

    match tier:
      case "Gold":
        cash_back = (15/100)*purchase_amount
      case "Silver":
        cash_back =  (10/100)*purchase_amount
      case "Bronze":
        cash_back = (5/100)*purchase_amount
      case _:
        print("No Cash Back")
        
    print("Cash Back earned: ", cash_back)
    print("=========================================")


def age_based_offer():
    print("===================================")
    age = int(input("Enter your age: "))
    member = input("Are you a member: ")
    print("==========================================================")

    if age < 13:
       if member == "yes":
        print("Kids Offer: Free toy on purchase above $500 + Priority Biling counter")
       else: 
        print("Kids Offer: Free toy on purchase above $500")
    elif age >= 13 and age < 20:
       if member == "yes":
        print("Teen offer: 10 percent off on stationary + Priority Biling counter")
       else: 
        print("Teen offer: 10 percent off on stationary")
    elif age >= 20 and age < 60:
      if member == "yes":
        print("Adult Offer: Standard discounts apply + Priority Biling counter")
      else: 
        print("Adult Offer: Standard discounts apply")    
    elif age >= 60:
        if member == "yes":
            print("Adult Offer: Standard discounts apply + Priority Biling counter")
        else: 
            print("Senior Citizen Offer: Extra 15 percent discount.")
            
    print("=================================================================")
    
    
        


print("========================================")
print("1. Calculate Discount")
print("2. Check membership cashback")
print("3. Check age based offer")
print("4. Exit")
print("========================================")



exit = True

while exit:
    choice = int(input("Enter your choice: "))
    match choice:
       case 1:
        calculate_discount()
       case 2:
        check_membership()
       case 3:
        age_based_offer()
       case 4:
           exit = False
       case _:
            print("Invalid choice. Please select 1-4.")
        
        
        
    
