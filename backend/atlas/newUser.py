import pymongo
from pymongo import MongoClient
import datetime
import connect


client = connect.getClient()

db = client['madhacks']


people = db.people

def newUser(InputName, userID):
    fname, lname = InputName.split()
    if people.find_one({ "name.last": lname, "name.first": fname }) == None:
        personDocument = {
        "name": { "first": fname, "last": lname },
        "id": userID,
        }
        people.insert_one(personDocument)
        return 1
    return 0

print(newUser("Henry Olig", 39))