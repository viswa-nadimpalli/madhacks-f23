import pymongo
import connect
import getUser



db.ProductData.update_one(
  { '_id': p['_id'] }
  ,
  { '$set': { 'd.a': existing + 1 } }
  , 
  upsert=False)

def insertQuiz(ID, )