import sqlite3




def findDetails(idToFind):
    print("Connecting to database...")
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row["id"] == idToFind:
            surferAttribsHash = {}
            surferAttribsHash["id"] = str(row["id"])
            surferAttribsHash["name"] = row["name"]
            surferAttribsHash["country"] = row["country"]
            surferAttribsHash["average"] = str(row["average"])
            surferAttribsHash["board"] = row["board"]
            surferAttribsHash["age"] = str(row["age"])
            cursor.close()
            return(surferAttribsHash)
        cursor.close()
        return({})



lookupID= int(input("Please input a surfer ID to retrieve a surfer's attributes:"))
surferToFind = findDetails(lookupID)

if surferToFind:
    print("Returning attributes for surfer with entered ID...")
    print("ID: " + surferToFind["id"])
    print("Name: " + surferToFind["name"])
    print("Country: " + surferToFind["country"])
    print("Average: " + surferToFind["average"])
    print("Board type: " + surferToFind["board"])
    print("Age: " + surferToFind["age"])