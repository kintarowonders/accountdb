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

    if (not ctype):
        print("You must specify a contact type.")
        return
    if (not detail):
        print("You must specify a contact detail.")
        return

    database.addContact(user, ctype, detail)
    print("Contact detail added to database.")

def renameUser(user):
    print("Renaming user.")
    newname = input('New username: "')
    
    if (not newname):
        print("You must specify a new username.")
        return

    changeUser(user, 0, "", newname)

def searchContact():
    ctype = input('Contact type: ')
    detail = input('Contact detail: ')
    
    uid = database.searchContact(ctype, detail)
    user = database.getContactById(uid)
    
    if (uid == -1):
        print("No such contact")
    else:
        print("Contact belongs to " + user + ".")
        showUser(user)

def modifyContact(user):
    print("Modifying contact detail.")
    showUser(user)
    ctype = input('Contact type to change: ')
    detail = input('New contact detail: ')
    if (database.changeContact(user, ctype, detail, "")):
        print("User modified")
    else
        print("User modification failed")

if (argv.length == 1):
    print("You didn't specify any command line arguments.")
    sys.exit()

def modifyUserDue(user):
    print("Modifying user due date.")
    newdate = input("Specify a date YYYY-MM-DD or an duration, eg: D1, W1, M1: ")

    if (not newdate):
        print ("You must specify a date or duration")
        return

    due = database.getUserDue(user)

    x = 0
    days = False
    weeks = False
    months = False
    doDuration = False
    durationString = ""
    for c in newdate:
        if (x == 0):
            if (newdate[0] == "D"):
                days = True
                doDuration = True
            if (newdate[0] == "W"):
                weeks = True
                doDuration = True
            if (newdate[0] == "M"):
                months = True
                doDuration = True
            if (x >= 1):
                if (doDuration):
                    durationString = durationString + c
   if (doDuration):
        durationInt = int(durationString)
        if (days):
            seconds = durationInt * 24 * 60 * 60
        if (weeks)
            seconds = durationInt * 7 * 24 * 60 * 60
        if (months)
            seconds = durationInt * 31 * 24 * 60 * 60
        due = due + seconds
    else:
        year, month, day = map(int, date_entry.split('-'))
        due = datetime.date(year, month, day)

    database.changeUser(user, due, "", "")   
    print("Database updated!")

def changeUserType(user):
    print("Changing customer type.")
    newtype = input("New type: ")
    
    if (not newtype):
        print("You must specify a new type.")
        return

    database.changeUser(user, 0, newtype, "")

#argument handler
success = False
if (argv[1] == "show"):
    if (argv.length != 4):
        print("Invalid number of arguments.")
        sys.exit()
    if (argv[2] == "user"):
        showUser(argv[3])
        success = True
    if (not success):
        print("Invalid arguments")
        sys.exit()
    sys.exit()
if (argv[1] == "edit"):
   
if (argv[1] == "add"):

if (argv[1] == "remove"):

if (argv[1] == "bill"):
    showDueBills()
