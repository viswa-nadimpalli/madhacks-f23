from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

import sys
import os

def getClient():
    mongodbkey = os.getenv("MONGODBKEY")
    client = MongoClient(mongodbkey)
    db = client['madhacks']
    people = db.people
    ppl = people.find_one({ "name.last": "Olig", "name.first": "Henry" })
    return ppl

print(getClient())