import os
import datetime
clock = {}
def clockIn(user):
    clock[user] = datetime.datetime.now()

def clockOut(user):
    #DB layout UserID(string), Clock in(DateTime), Clock out(DateTime), totalTime
    server.query("INSERT INTO time VALUES (?, ?, ?)", user, clock[user] , datetime.datetime.now())
    del clock[user]

def runReport():
    return 

def runUserReport(user):
    return server.query("SELECT * FROM time WHERE UserID = (?)", user)