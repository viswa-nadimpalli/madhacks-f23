import pymongo
import connect
from pymongo import MongoClient
import datetime


client = connect.getClient()


db = client.gettingStarted


people = db.people

def getUser(InputName):
    fname, lname = InputName.split()
    return people.find_one({ "name.last": lname, "name.first": fname })

print(getUser("Henry Olig"))

# personDocument = {
#   "name": { "first": "Alan", "last": "Turing" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }

# people.insert_one(personDocument)



