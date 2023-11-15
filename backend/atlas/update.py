import pymongo
import connect
import getUser
import datetime
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
import ssl
load_dotenv()

import sys
import os


# db.ProductData.update_one(
#   { '_id': p['_id'] }
#   ,
#   { '$set': { 'd.a': existing + 1 } }
#   , 
#   upsert=False)

def insertQuiz(ID, text):
  try:
    ca = certifi.where()
    # try:
    # client = connect.getClient()
    mongodbkey = os.getenv("MONGODBKEY")
    client = MongoClient(mongodbkey, tls=True)
    db = client.madhacks
    people = db.people
    x = datetime.datetime.now()
    dt = x.strftime("%x")+"-"+x.strftime("%X")
    # print('This is error output', file=sys.stderr)
    currentFiles = people.find_one({ "id": ID })['quizzes']
    currentFiles[dt] = text
    people.update_one(
        { "id": ID }
        ,
        { "$set": { "quizzes" : currentFiles } }
        ,
        bypass_document_validation=True,
        upsert=True
    )
    return "1"
  except:
    return "0"
  # except e:
  #   print("An error occured!")
  #   print(e)
  #   return "0"