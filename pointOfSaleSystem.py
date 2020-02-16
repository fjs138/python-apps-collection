# Application Description:
# The POS program will record credit card sales in a file called transactions.txt
# Each line starts with 16 characters of credit card number followed by the next
# 7 characters showing the price. The description follows that, spaced to right justification
# Example 1: 62189672574056180000220 LATTE
# Example 2: 42657423454758780000095 GRAIN BAR
# ($1.75 is written as 0000175)

# This line needs to be added to any program that uses the transactions.py module
# the word transactions here means run the code in the module called
# transactions.py the * here means treat everything inside the module as
# if it is code within your # program
from transactions import *

#print("There are %5d %s available" % (17, "donuts"))
print("************")
print("TESTING...")
print("************")
def outputAvailable(d, s):
    print("There are %5d %s available" % (d, s))
outputAvailable(22, "cheeses")
print()

print()
print("*************************")
print("WELCOME TO THE POS SYSTEM")
print("*************************")


# here is the function for processing transactions
# transactionsTXT will use credit_card ,  price , and  description /n
# see transactions.py


# this is the array of available menu options:
purchases = ["DONUT", "LATTE", "FILTER", "MUFFIN"]

#this is the matching array of menu prices for the above options
purchasePrice = [1.50, 2.0, 1.80, 1.20]

transactionInProgress = True

# the loop will keep running while the transactionInProgress variable
# has the value True. To end the loop, set transactionInProgress to False.
while transactionInProgress:
    option = 1
    for choice in purchases:
        # this code displays the program's menu.
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    # the user enters a menu option number to make a sale.
    choice = int(input("Choose an option: "))
    if choice == option:
        transactionInProgress = False
    else:
        creditCard = input("Credit card number: ")
        saveTransacation(purchasePrice[choice - 1], int(creditCard), purchases[choice - 1])