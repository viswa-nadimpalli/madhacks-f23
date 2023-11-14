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
  ca = certifi.where()
  # try:
  # client = connect.getClient()
  mongodbkey = os.getenv("MONGODBKEY")
  client = MongoClient(mongodbkey)
  db = client.gettingStarted
  people = db.peoples
  x = datetime.datetime.now()
  dt = x.strftime("%x")+"-"+x.strftime("%X")
  # print('This is error output', file=sys.stderr)
  people.update_one(
      { "id": ID }
      ,
      { "$set": { dt: text } }
  )
  return "1"
  # except e:
  #   print("An error occured!")
  #   print(e)
  #   return "0"
  
insertQuiz('google-oauth2|102485158041172712830', "gottat test this man")