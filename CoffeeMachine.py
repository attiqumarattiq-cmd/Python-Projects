
logo = '''
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

profit =  0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

menuprint ='''
        ============== MENU ============
        [1]: PRINT STATUS REPORT
        [2]: ORDER ESPRESSO
        [3]: ORDER LATTE 
        [4]: ORDER CAPPUCCCINO
        [5]: EXIT
        =================================
        
'''

MENU = {
    "espresso":{
        "ingredients":{
            "water": 200,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 250,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def calculatemoney():
    quarters = int(input("How many quarters? : ")) # 25 cent, 0.25 dollor
    dimes = int(input("How many dimes? : "))       # 10 cent, 0.10 dollar
    nickels = int(input("How many nickels? : "))   # 5 cent, 0.05 dollor
    pennies = int(input("How many pennies? : "))   # 1 cent, 0.01 dollar
    return round((pennies*0.01)+(nickels*0.05)+(dimes*0.10)+(quarters*0.25))
    







# MAIN CODE TO RUN
print(logo)
keepgoing = True
while keepgoing:
    waterleft = resources["water"]
    milkleft = resources["milk"]
    coffeeleft = resources["coffee"]
    
    print(menuprint)
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f'''
            === STATUS REPORT ===
            Water: {waterleft}ml
            Milk: {milkleft}ml
            Coffee: {coffeeleft}ml
            Profit: ${profit}
              ''')
    elif choice == 2:
        money = calculatemoney()
        
        waterreq = MENU["epresso"]["ingredients"]["water"]
        coffeereq = MENU["espresso"]["ingredients"]["coffee"]
        cost = MENU["espresso"]["cost"]
        
        if money >= cost and waterreq <= waterleft and coffeereq <= coffeeleft:
            change = money - cost
            profit = profit + cost
            resources["water"] = resources["water"] - waterreq
            resources["coffee"] = resources["coffee"] - coffeereq
            
            if change >= 0:
                print(f"Your change: ${change}")
                print("Enjoy your espresso !")
        elif waterreq > waterleft or coffeereq > coffeeleft:
            print("Sorry, the machine does not enough ingredients!")
        else:
            print("Sorry, You did not put enough money ! Here is your refund !")
        
    elif choice == 3:
        money = calculatemoney()
        
        waterreq =  MENU["latte"]["ingredients"]["water"]
        milkreq = MENU["latte"]["ingredients"]["milk"]
        coffeereq = MENU["latte"]["ingrredients"]["coffee"]
        cost = MENU["latte"]["cost"]
        
        if money >= cost and waterreq <= waterleft and milkreq <= milkleft and coffeereq <= coffeeleft:
            change = money - cost
            profit = profit + cost
            resources["water"] = resources["water"] - waterreq
            resources["milk"] = resources["milk"] - milkreq
            resources["coffee"] = resources["coffee"] - coffeeleft
            
            if change >= 0:
                print(f"Your change: ${change}")
                print("Enjoy your latte !")
        
        elif waterreq > waterleft or milkreq > waterleft or coffeereq > waterleft:
            print("Sorry, the machine does not enough ingredients!")
        else:
            print("Sorry, You did not put enough money ! Here is your refund !")
                      
    elif choice == 4:
        money = calculatemoney()
        
        waterreq = MENU["cappuccino"]["ingredients"]["water"]
        milkreq =  MENU["cappuccino"]["ingredients"]["milk"]
        coffeereq = MENU["cappuccino"]["ingredients"]["coffee"]
        
        
        
        
    
    
    
