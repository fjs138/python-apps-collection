from transactions import *
# import transactions processing module

import promotion
# import promotional discount module

import starbuzz
# import starbuzz discount module

items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
running = True
while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option += 1
        # same as option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        price = promotion.discount(prices[choice - 1])
        # utilizing the promotional discount code
        if input("Starbuzz card? ") == "Y":
            price = starbuzz.discount(price)
            print("Applying Starbuzz discount...")
        else:
            print("Not applying Starbuzz discount...")
        save_transaction(price, credit_card, items[choice - 1])

        # saveTransacation(purchasePrice[choice - 1], int(creditCard), purchases[choice - 1])
        # saveTransaction(purchasePrice[choice - 1], int(creditCard), purchases[choice - 1])