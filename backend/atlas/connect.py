from dotenv import load_dotenv
from pymongo import MongoClient
import connect
load_dotenv()

import sys
import os

def getClient():
    mongodbkey = os.getenv("MONGODBKEY")
    client = MongoClient('mongodb+srv://olig0007:8H1fapZ86Z5l7D7y@cluster0.cqo5ajt.mongodb.net/?retryWrites=true&w=majority')
    return client

