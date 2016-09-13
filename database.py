import globalVars
import tempfile
import shutil
import os

def getContactByType(uidIn, typeIn):
    f = open(globalVars.contactDatabase, 'r')
    for line in f:
        splitted = line.split(',')
        index = int(splitted[0])
        userId = int(splitted[1])
        contactType = splitted[2]
        contactDetail = splitted[3]
        if (uidIn == userId):
            if (typeIn == contactType):
                return contactDetail.strip('\n')
    return "%%NOTFOUND%%"

def getContactById(uidIn, cidIn):
    f = open(globalVars.contactDatabase, 'r')
    for line in f:
        splitted = line.split(',')
        index = int(splitted[0])
        userId = int(splitted[1])
        contactDetail = splitted[3]
        if (uidIn == userId):
            if (cidIn == index):
                return contactDetail.strip('\n')
    return "%%NOTFOUND%%" 

def getContactType(uidIn, cidIn):
    f = open(globalVars.contactDatabase, 'r')
    for line in f:
        splitted = line.split(',')
        index = int(splitted[0])
        userId = int(splitted[1])
        contactType = splitted[2]
        if (uidIn == userId):
            if (cidIn == index):
                return contactType
    return "%%NOTFOUND%%"

def getUserId(userIn):
    f = open(globalVars.userDatabase, 'r') 
    for line in f:
        splitted = line.split(',')
        index = int(splitted[0])
        userName = splitted[1]
        if (userName == userIn):
            return index
    return -1

def getUserName(uidIn):
    f = open(globalVars.userDatabase, 'r')
    for line in f:
        splitted = line.split(',')
        index = int(splitted[0])
        userName = splitted[1]
        if (uidIn == index):
            return userName
    return "%%NOTFOUND%%"

def getUserDue(uidIn):
    f = open(globalVars.userDatabase, 'r')
    for line in f:
        splitted = line.split(',')
        index = int(splitted[0])
        userDue = int(splitted[2])
        if (uidIn == index):
            return userDue
    return -1

def getUserType(uidIn):
    f = open(globalVars.userDatabase, 'r')
    for line in f:
        splitted = line.split(',')
        index = int(splitted[0])
        userType = splitted[3]
        if (uidIn == index):
            return userType
    return "%%NOTFOUND%%"

def getUserList():
    f = open(globalVars.userDatabase, 'r')
    l = []
    for line in f:
        splitted = line.split(',')
        l.append(int(splitted[0]))
    return l

def getContactList(uidIn):
    f = open(globalVars.contactDatabase, 'r')
    l = []
    for line in f:
        splitted = line.split(',')
        userId = int(splitted[1])
        if (userId == uidIn):
            l.append(int(splitted[0]))
    return l

def addContact(userIn, typeIn, detailIn):
    # first we scan existing indexes, to work out the next index point
    skipIndexSearch = False
    try:
        f = open(globalVars.contactDatabase, 'r')
    except FileNotFoundError:
        skipIndexSearch = True
    if (not skipIndexSearch):
       for line in f:
           splitted = line.split(',')
           index = int(splitted[0])
       index = index + 1 
    else:
       index = 0
    w = open(globalVars.contactDatabase, 'a')
    w.write(str(index) + "," + str(userIn) + ',' + typeIn + ',' + detailIn + '\n')

def addUser(userName, nextDue, serviceType):
    # first we scan existing indexes, to work out the next index point
    skipIndexSearch = False
    try:
        f = open(globalVars.userDatabase, 'r')
    except FileNotFoundError:
        skipIndexSearch = True
    if (not skipIndexSearch):
       for line in f:
           splitted = line.split(',')
           index = int(splitted[0])
       index = index + 1
    else:
       index = 0
    w = open(globalVars.userDatabase, 'a')
    w.write(str(index) + "," + userName + "," + str(nextDue) + "," + serviceType + '\n')

def replace(file_path, pattern, subst):
    #Create temp file
    #Code from: https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
    fh, abs_path = tempfile.mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    os.close(fh)
    #Remove original file
    os.remove(file_path)
    #Move new file
    shutil.move(abs_path, file_path)

def changeUser(userName, nextDue, serviceType, newName):
    f = open(globalVars.userDatabase, "r")
    oldline = ""
    for line in f:
        splitted = line.split(",")
        index = int(splitted[0])
        user = splitted[1]
        due = splitted[2]
        serivce = splitted[3]
        if (splitted[1] == userName):
            oldline = line
            break
    f.close()
    if (not oldline):
        return False
    if (nextDue != 0):
        due = nextDue
    if (newName):
        user = newName
    if (serviceType):
        service = serviceType
    newline = str(index) + "," + user + "," + str(due) + "," + service + '\n'
    replace(globalVars.userDatabase, oldline, newline)
    return True

def deleteUser(uid)
    f = open(globalVars.userDatabase, "r")
    lines = f.readlines()
    f.close()
    w = open(globalVars.userDatabase, "w")
    for line in lines:
        splitted = line.split(',')
        if (int(splitted[0]) != uid):
            f.write(line)
    w.close()

def changeContact(userIn, typeIn, detailIn, newName):
    f = open(globalVars.contactDatabase, "r")
    oldline = ""
    for line in f:
        splitted = line.split(',')
        index = int(splitted[0])
        user = splitted[1]
        ctype = splitted[2]
        detail = splitted[3]
        if (spitted[1] == userIn):
            oldline = line
            break
    f.close()
    if (not oldline):
        return False
    if (typeIn):
        ctype = typeIn
    if (detailIn):
        detail = detailIn
    if (newName):
        user = newName
    newline = str(index) + "," + user + "," + ctype + ',' + detail + '\n'
    replace(globalVars.contactDatabase, oldline, newline)
    return True

def deleteContact(cid):
    f = open(globalVars.contactDatabase,'r')
    lines = f.readlines()
    f.close()
    w = open(globalVars.contactDatabase,'w')
    for line in lines:
        splitted = line.split(',')
        if (int(splitted[0]) != cid):
            f.write(line)
    w.close()
