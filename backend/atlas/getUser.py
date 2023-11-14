import pymongo
import connect
from pymongo import MongoClient
import datetime



def fetchUser(ID):
    client = connect.getClient()
    db = client.gettingStarted
    people = db.people
    return people.find_one({ "id": ID })



# personDocument = {
#   "name": { "first": "Alan", "last": "Turing" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }

# people.insert_one(personDocument)



