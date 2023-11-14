import pymongo
from pymongo import MongoClient
import datetime
import connect
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/newUser/<InputName>/<userID>', methods=['POST'])


def newUser(InputName, userID):
    client = connect.getClient()
    db = client['madhacks']
    people = db.people
    fname, lname = InputName.split()
    if people.find_one({ "name.last": lname, "name.first": fname }) == None:
        personDocument = {
        "name": { "first": fname, "last": lname },
        "id": userID,
        "quizzes": {}
        }
        people.insert_one(personDocument)
        return "ok"
    return "0"

if __name__ == '__main__':
    app.run(debug=True)