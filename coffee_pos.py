"""# Application Description:
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

# import transactions processing module
# from transactions import *
import promotion
# import promotional discount module
# from promotion import *
import starbuzz
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
        # option += 1 is a shorter, "augmented" version
    print(str(option) + ". Quit")
    # the user enters a menu option number to make a sale.
    choice = int(input("Choose an option: "))
    if choice == option:
        transactionInProgress = False
    else:
        creditCard = input("Credit card number: ")
        # utilizing the promotional discount code
        price = promotion.discount(prices[choice - 1])
        if input("Starbuzz card?")=="Y":
            price = starbuzz.discount(price)
        saveTransacation(price, creditCard, purchases[choice - 1])

        # saveTransacation(purchasePrice[choice - 1], int(creditCard), purchases[choice - 1])
        # save_transaction(prices[choice - 1], credit_card, items[choice - 1])
        """

from transactions import *
# import transactions processing module

import promotion
# import promotional discount module

import starbuzz
# import starbuzz discount module


items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
running = True
while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option += 1
        # can be replaced with: option += 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        price = promotion.discount(prices[choice - 1])
        if input("Starbuzz card? ") == "Y":
            price = starbuzz.discount(price)
            print("Applying Starbuzz discount...")
        else:
            print("Not applying Starbuzz discount...")
        save_transaction(price, credit_card, items[choice - 1])