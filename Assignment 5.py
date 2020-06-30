import sqlite3

#connecting database

database = sqlite3.connect("assignment2.db")

#cursor to work with

cursor = database.cursor()

class user:
    def __init__(self,fname,lname,tempID):
        self.firstname = fname
        self.lastname = lname
        self.ID = tempID

    def printthis(self):
        print("First Name: ", self.firstname, " Last Name: ", self.lastname, " ID: ", self.ID)

    def searchcourseall(self):
        print("Entire table")
        cursor.execute("""SELECT * FROM COURSE""")
        query_result = cursor.fetchall()

        for i in query_result:
            print(i)

    def searchcoursebyCRN(self):
        crn = str(input('Enter CRN to search: '))
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s'""" % crn)
        query_result = cursor.fetchall()

        for i in query_result:
            print(i)

        if bool(query_result) == 0:
            print("No Course available with this CRN!")


class student(user):
    def __init__(self,fname,lname,tempID,gradyear,major,email):
        super().__init__(fname,lname,tempID)
        self.graduationyear = gradyear
        self.major = major
        self.email = email

    def addcourse(self,email):
        CRN = input('Enter A CRN to Add to your Schedule: ')

        query_result = cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s'""" % CRN)
        if query_result == []:
            print('CRN does not exist!')

        else:
            cursor.execute("""INSERT INTO STUDENTCOURSE VALUES ('%s','%s')"""  % (email,CRN))

    def dropcourse(self):
        CRN = input('Enter CRN to remove: ')
        cursor.execute("""DELETE FROM STUDENTCOURSE WHERE CRN = '%s'""" % CRN)

    def printschedule():
        pass


class instructor(user):
    def __init__(self, fname, lname, tempID,title,hireyear,dept,email):
        super().__init__(fname, lname, tempID)
        self.title = title
        self.hireyear = hireyear
        self.department = dept
        self.email = email

    def printschedule():
        pass
    def printroster():
        pass
    def searchcourses():
        pass

class admin(user):
    def __init__(self, fname, lname, tempID,title,office,email):
        super().__init__(fname,lname,tempID)
        self.title = title
        self.office = office
        self.email = email

    def addcourses(self):
        title = input('Enter Title: ')
        crn = input('Enter CRN: ')
        dept = input('Enter Department: ')
        inst = input('Enter Instructor: ')
        time = input('Enter Time: ')
        days = input('Enter Days: ')
        sem = input('Enter Semester: ')
        year = input('Enter Year: ')
        cred = input('Enter Credits: ')
        cursor.execute("""INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (title, crn, dept, inst, time, days, sem, year, cred))

    def removecourses(self):
        crn = input('Enter CRN to remove the course: ')
        cursor.execute("""DELETE FROM COURSE WHERE CRN = '%s'""" % crn)

    def adduser(self):
        choice = input('What do you want to add?\n 1.Student\n 2.Instructor\n 3.Admin\n')
        choice = int(choice)

        # if they want to add a new student
        if choice == 1:
            uid = input('Enter ID: ')
            fname = input('Enter First Name: ')
            lname = input('Enter Last Name: ')
            gradyear = input('Enter Graduation Year: ')
            major = input('Enter Major: ')
            email = input('Enter Email: ')
            cursor.execute("""INSERT INTO STUDENT VALUES('%s', '%s', '%s', '%s', '%s', '%s')""" % (
            uid, fname, lname, gradyear, major, email))

        # if they want to add a new instructor
        if choice == 2:
            uid = input('Enter ID: ')
            fname = input('Enter First Name: ')
            lname = input('Enter Last Name: ')
            title = input('Enter Title: ')
            hireyear = input('Enter Hire Year: ')
            dept = input('Enter Department: ')
            email = input('Enter Email: ')
            cursor.execute("""INSERT INTO INSTRUCTOR VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
            uid, fname, lname, title, hireyear, dept, email))

        # if they want to add a new admin
        if choice == 3:
            uid = input('Enter ID: ')
            fname = input('Enter First Name: ')
            lname = input('Enter Last Name: ')
            title = input('Enter Title: ')
            office = input('Enter Office Location: ')
            email = input('Enter Email: ')
            cursor.execute("""INSERT INTO ADMIN VALUES('%s', '%s', '%s', '%s', '%s', '%s')""" % (
            uid, fname, lname, title, office, email))

    def removeuser():
        choice = input('What do you want to remove?\n 1.Student\n 2.Instructor\n 3.Admin\n')
        choice = int(choice)

        if choice == 1:
            email = input('Enter an email to remove the entry: ')
            cursor.execute("""DELETE FROM STUDENT WHERE EMAIL = '%s'""" % email)

        if choice == 2:
            email = input('Enter an email to remove the entry: ')
            cursor.execute("""DELETE FROM INSTRUCTOR WHERE EMAIL = '%s'""" % email)

        if choice == 3:
            email = input('Enter an email to remove the entry: ')
            cursor.execute("""DELETE FROM ADMIN WHERE EMAIL = '%s'""" % email)

    def forcein():
        pass
    def forceout():
        pass
    def searchprintroster():
        pass

########################### MAIN ################################################

login = input('Who are you logging in as?\n1.Student\n2.Instructor\n3.Admin\n')
login = int(login)
if login == 1:
    username = str(input('Enter your email: '))
    cursor.execute("""SELECT * FROM STUDENT WHERE EMAIL = '%s'""" % username)
    query_result = cursor.fetchall()
    query = bool(query_result)
    if query == 1:
        cursor.execute("""SELECT ID FROM STUDENT WHERE EMAIL = '%s'""" % username)
        ID = cursor.fetchall()
        cursor.execute("""SELECT NAME FROM STUDENT WHERE EMAIL = '%s'""" % username)
        name = cursor.fetchall()
        cursor.execute("""SELECT SURNAME FROM STUDENT WHERE EMAIL = '%s'""" % username)
        surname = cursor.fetchall()
        cursor.execute("""SELECT GRADYEAR FROM STUDENT WHERE EMAIL = '%s'""" % username)
        gradyear = cursor.fetchall()
        cursor.execute("""SELECT MAJOR FROM STUDENT WHERE EMAIL = '%s'""" % username)
        major = cursor.fetchall()
        cursor.execute("""SELECT EMAIL FROM STUDENT WHERE EMAIL = '%s'""" % username)
        email = cursor.fetchall()
        x = student(name, surname, ID, gradyear, major, email)
        courseschedule = []

        while True:
            choice = input('1.SEARCH\n2.SEARCHALL\n3.ADD\n4.REMOVE\n5.PRINT\n6.LOGOUT\n')
            choice = int(choice)


            if choice == 1:
                x.searchcoursebyCRN()
            elif choice == 2:
                x.searchcourseall()
            elif choice == 3:
                x.addcourse(username)
                database.commit()
            elif choice == 4:
                x.dropcourse()
                database.commit()

            if choice == 6:
                break

    else:
        print('User does not exist! ')

elif login == 2:
    username = str(input('Enter your email: '))
    cursor.execute("""SELECT * FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
    query_result = cursor.fetchall()
    query = bool(query_result)
    if query == 1:
        cursor.execute("""SELECT ID FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
        ID = cursor.fetchall()
        cursor.execute("""SELECT NAME FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
        name = cursor.fetchall()
        cursor.execute("""SELECT SURNAME FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
        surname = cursor.fetchall()
        cursor.execute("""SELECT TITLE FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
        title= cursor.fetchall()
        cursor.execute("""SELECT HIREYEAR FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
        hireyear = cursor.fetchall()
        cursor.execute("""SELECT DEPT FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
        dept = cursor.fetchall()
        cursor.execute("""SELECT EMAIL FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
        email = cursor.fetchall()
        x = instructor(name,surname,ID,title,hireyear,dept,email)

        while True:
            choice = input('1.SEARCH COURSE BY CRN\n2.SEARCH ALL COURSES\n3.PRINT COURSE ROSTER\n4.PRINT INSTRUCTOR SCHEDULE\n5.LOGOUT\n')
            choice = int(choice)


            if choice == 1:
                x.searchcoursebyCRN()
            elif choice == 2:
                x.searchcourseall()
            if choice == 5:
                break
    else:
        print("User does not exist!")

elif login == 3:
    username = str(input('Enter your email: '))
    cursor.execute("""SELECT * FROM ADMIN WHERE EMAIL = '%s'""" % username)
    query_result = cursor.fetchall()
    query = bool(query_result)
    if query == 1:
        cursor.execute("""SELECT ID FROM ADMIN WHERE EMAIL = '%s'""" % username)
        ID = cursor.fetchall()
        cursor.execute("""SELECT NAME FROM ADMIN WHERE EMAIL = '%s'""" % username)
        name = cursor.fetchall()
        cursor.execute("""SELECT SURNAME FROM ADMIN WHERE EMAIL = '%s'""" % username)
        surname = cursor.fetchall()
        cursor.execute("""SELECT TITLE FROM ADMIN WHERE EMAIL = '%s'""" % username)
        title = cursor.fetchall()
        cursor.execute("""SELECT OFFICE FROM ADMIN WHERE EMAIL = '%s'""" % username)
        office = cursor.fetchall()
        cursor.execute("""SELECT EMAIL FROM ADMIN WHERE EMAIL = '%s'""" % username)
        email = cursor.fetchall()
        x = admin(name,surname,ID,title,office,email)
        while True:
            choice = input('1.Add a Course\n2.Remove A Course\n3.Search All Courses\n4.Search by CRN\n5.Add User\n6.Remove User\n7.Assign Course to Instructor\n8.LOGOUT\n')
            choice = int(choice)

            if choice == 1:
                x.addcourses()
                database.commit()
            elif choice == 2:
                x.removecourses()
                database.commit()
            elif choice == 3:
                x.searchcourseall()
            elif choice == 4:
                x.searchcoursebyCRN()
            elif choice == 8:
                break

    else:
        print("User does not exist!")


database.commit()

# close the connection
database.close()






