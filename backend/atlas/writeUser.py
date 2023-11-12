import getUser
import pymongo
import connect

client = connect.getClient()

db = client.gettingStarted
people = db.people


def writeUser(user, info):
    if getUser(user) is not None:
        ...

    return 0