from atlas import *
# import getUser
# import writeUser
# import update
# import connect


def getUser(ID):
    return getUser.fetchUser(ID)

def newUser(ID):
    return newUser.newUser(ID)

def getClient():
    return connect.getClient()

def add_quiz(ID, text):
    return update.insertQuiz(ID, text)
