import database
import sys
import time
import datetime

def showDueBills():
    currentTime = time.time()
    
    for user in database.getUserList:
        due = database.getUserDue(user)
        username = database.getUserName(user)
        if (currentTime > due):
            print(username + " is due.")

def showUserContact(user):
    uid = database.getUserId(user)
    
    if (uid == -1):
        print "No such user."
        return 1

    print("Contact details for user: " + user)
    contacts = database.getContactList(uid)

    for contact in contacts:
        contactDetail = database.getContactById(uid, contact)
        contactType = database.getContactType(uid, contact)
        print(contactType + ": " + contactDetail)

def showUser(user):
    uid = database.getUserId(user)

    if (uid == -1):
        print "No such user."
        return 1

    timestamp = database.getUserDue(uid)
    datestamp  = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    print("User " + user + " due " + datestamp + ".")
    showUserContact(user)

def addUser(user):
    date_entry = input('Enter a due date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    due = datetime.date(year, month, day)
    
    email = input('Enter an email address: ')
    service = input('Enter service type: ')
    
    duestamp = due.timestamp()
    database.addUser(user, due, service)
    database.addContact(user, "email", email)

def addUserContact(user):
    ctype = input('Contact type: ')
    detail = input('Contact detail: ')
    database.addContact(user, ctype, detail)

    
