
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
    
    
    
