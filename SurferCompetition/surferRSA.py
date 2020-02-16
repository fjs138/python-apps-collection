

def findDetails(idToFind):
    print("Opening data file...")
    rsaCSV = open("surfing_data.csv")
    for eachLine in rsaCSV:
        surferInfo = {}
        (surferInfo["id"], surferInfo["name"], surferInfo["country"], surferInfo["average"],surferInfo["board"], surferInfo["age"]) = eachLine.split(";")
        if idToFind == int(surferInfo["id"]):
            print("Match found! Closing data file...")
            rsaCSV.close()
            return(surferInfo)
    print("No match found! Closing data file...")
    rsaCSV.close()
    return({})

lookupID= int(input("What surfer ID to look up?"))
surferToFind = findDetails(lookupID)

if surferToFind:
    print("ID: " + surferToFind["id"])
    print("Name: " + surferToFind["name"])
    print("Country: " + surferToFind["country"])
    print("Average: " + surferToFind["average"])
    print("Board type: " + surferToFind["board"])
    print("Age: " + surferToFind["age"])

