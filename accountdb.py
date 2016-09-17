import database
import sys
import time

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
        return -1
    print("Contact details for user: " + user)
    contacts = database.getContactList(uid)
    for contact in contacts:
        contactDetail = database.getContactById(uid, contact)
        contactType = database.getContactType(uid, contact)
        print(contactType + ": " + contactDetail)
