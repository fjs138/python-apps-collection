# def saveTransacation(purchasePrice, creditCard, purchaseDescription):
def save_transaction(price, credit_card, description):

    print("***********************************")
    print("*****TRANSACATIONS IN PROGRESS*****")
    print("Utilizing transactions.py module...")
    print("***********************************")
    print("Opening transactions.txt for file output...")
    # the "a" below means that you are going to append
    # each record to the end of the file
    file = open("transactions.txt", "a")
    # transactionsTXT = open("transactions.txt", "a")
    print("transactions.txt opened successfully.")
    # old formatting:
    # transactionsTXT.write("%s%07d%s\n" % (creditCard, purchasePrice * 100, purchaseDescription))
    # corrected new formatting:
    # old incorrect?
    # transactionsTXT.write("%07d%16s%16s\n" % (creditCard, purchasePrice * 100, purchaseDescription))

    # this doesnt combine first two parts
    file.write("%07d%16s%16s\n" % (price * 100, credit_card, description))
    # this includes decimal
    # transactionsTXT.write("%s%07d%16s\n" % (purchasePrice * 100, creditCard, purchaseDescription))


    # the format specifier %16s adds padding so we get 1242134213   MUFFINS
    # instead of 1242134213MUFFINS

    print()
    print("Closing transactions.txt...")
    file.close()
    print("transactions.txt closed successfully.")

""" def save_transaction(price, credit_card, description):
        file = open("transactions.txt", "a")
"""