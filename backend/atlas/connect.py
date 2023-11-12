from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

import sys
import os

def getClient():
    mongodbkey = os.getenv("MONGODBKEY")
    client = MongoClient(mongodbkey)
    return client

