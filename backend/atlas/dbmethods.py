from atlas import *
from atlas.updateUser import insertQuiz
from atlas.connect import getClient
# import getUser
# import writeUser
# import updateUser
# import connect


def getUser(ID):
    return getUser.fetchUser(ID)

def newUser(ID):
    return newUser.newUser(ID)

# def getClient():
#     return connect.getClient()

def add_quiz(ID, text):
    return insertQuiz(ID, text)
