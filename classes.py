import database

class user:
    def __init__(self, idnum, Fname, Lname):
        self.idnum = idnum
        self.Fname = Fname
        self.Lname = Lname

    def print(self):
        print("ID num: " + self.idnum + " - First Name:" + self.Fname + " - Last Name:" + self.Lname + " ")

    def setID(self, num):
        self.idnum = num

    def setFname(self, name):
        self.Fname = name

    def setLname(self, name):
        self.Lname = name


class student(user):
    def __init__(self, idnum, Fname, Lname, GradYear, Major, Email):
        super().__init__(idnum, Fname, Lname)
        self.GradYear = GradYear
        self.Major = Major
        self.Email = Email
    def print(self):
        database.cursor.execute("""SELECT * FROM COURSE""")
        query_result = database.cursor.fetchall()
        print("Current courses in the database")
        for i in query_result:
            print(i)

    def searchcourse(self):
        CRN = input("Enter the CRN code of the course you would like to search")
        sql_command = """SELECT 1 FROM COURSE WHERE CRN = """ + CRN + """;"""
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()
        if query_result == []:
            print("The CRN code does not exist")
            return
        else:
            sql_command = """SELECT TITLE FROM COURSE WHERE CRN = """+CRN+"""; """
            database.cursor.execute(sql_command)
            query_result = database.cursor.fetchall()
            for i in query_result:
                print(i)

        # connect to database

    def addCourse(self,id):
        CRN = input("Enter the CRN code of the course you would like to take")
        sId = str(id)
        sql_command = """SELECT 1 FROM COURSE WHERE CRN = """ + CRN + """;"""
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()
        if query_result == []:
            print("The CRN code does not exist")
            return
        else:

            database.cursor.execute("""INSERT INTO STUDENTCOURSE VALUES("""+sId+""","""+CRN+"""); """)
            sql_command = """SELECT DISTINCT COURSE.TITLE FROM COURSE,STUDENTCOURSE WHERE COURSE.CRN ="""+ CRN +""" ;"""
            database.cursor.execute(sql_command)
            query_result = database.cursor.fetchall()
            for i in query_result:
                print(i)
            print("Has been added to your courses\n")
            database.commit()
            return

        # connect to database
        # return course added

    def dropCourse(self, idnum):
        sidnum = str(idnum)
        CRN = input("Enter the CRN code of the course you would like to remove")
        sql_command = """SELECT 1 FROM COURSE WHERE CRN = """ + CRN + """;"""
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()

        if query_result == []:
            print("The CRN code does not exist")
            return
        else:
            sql_command = """SELECT 1 FROM STUDENTCOURSE WHERE STUDENTID = """+sidnum+""" AND CRN = """+CRN+"""; """
            database.cursor.execute(sql_command)
            query_result = database.cursor.fetchall()

            if query_result == []:
                print("The your not taking this course")
                return
            else:
                sql_command= """DELETE FROM STUDENTCOURSE WHERE STUDENTID = """ + sidnum + """ AND CRN = """ + CRN + """; """
                database.cursor.execute(sql_command)
                sql_command = """SELECT TITLE FROM COURSE WHERE CRN = """+CRN+"""; """
                database.cursor.execute(sql_command)
                query_result = database.cursor.fetchall()
                for i in query_result:
                    print(i)
                print(" Has been removed from your courses to your courses")
                database.commit()
                return

        # connect to database
        # return removed course

    def sprint(self,idnum):
        sidnum = str(idnum)
        sql_command = """SELECT STUDENTCOURSE.CRN FROM STUDENTCOURSE WHERE STUDENTID ="""+ sidnum +""" ;"""
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()
        print("Current courses enrolled in")
        for i in query_result:
            print(i)



class instructor(user):
    def __init__(self, idnum, Fname, Lname, title, hireyear, dept,email):
        super().__init__(idnum, Fname, Lname)
        self.title = title
        self.hireyear = hireyear
        self.dept = dept
        self.email = email

    def searchcourse(self):
        CRN = input("Enter the CRN code of the course you would like to search")
        sql_command = """SELECT 1 FROM COURSE WHERE CRN = """ + CRN + """;"""
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()
        if query_result == []:
            print("The CRN code does not exist")
            return
        else:
            sql_command = """SELECT TITLE FROM COURSE WHERE CRN = """ + CRN + """; """
            database.cursor.execute(sql_command)
            query_result = database.cursor.fetchall()
            for i in query_result:
                print(i)

    def print(self):
        database.cursor.execute("""SELECT * FROM COURSE""")
        query_result = database.cursor.fetchall()
        print("Current courses in the database")
        for i in query_result:
            print(i)

    def rosterprint(self, id):
        sid = str(id)
        sql_command = """SELECT DISTINCT STUDENTCOURSE.STUDENTID FROM STUDENTCOURSE,COURSE,INSTRUCTOR WHERE STUDENTCOURSE.CRN = COURSE.CRN AND COURSE.INSTRUCTORid = """+sid+"""; """
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()
        print("Current students  enrolled in your course")
        for i in query_result:
            print(i)

        # pass in course to database
        # print roster array


class admin(user):
    def __init__(self, idnum, Fname, Lname, title, office, email):
        super().__init__(idnum, Fname, Lname)
        self.title = title
        self.office = office
        self.email = email

    def print(self):
        database.cursor.execute("""SELECT * FROM COURSE""")
        query_result = database.cursor.fetchall()
        print("Current courses in the database")
        for i in query_result:
            print(i)

    def adminadd(self):
            dpt = input("What department are you adding the course to? insert '' marks for string inputs\n")
            sql_command = """SELECT INSTRUCTOR.ID,INSTRUCTOR.NAME, INSTRUCTOR.SURNAME FROM INSTRUCTOR WHERE INSTRUCTOR.DEPT = """ + dpt + """ ; 
                """
            print(sql_command)

            database.cursor.execute(sql_command)
            query_result = database.cursor.fetchall()
            print("Here are the available instructors from " + dpt + "\n")

            for i in query_result:
                print(i)
            id = input("Enter the available instructors id too add this instructor to the course\n")
            title = input("Enter the title of the course ''\n")
            CRN = input("Create the CRN code for this course")
            time = input("Enter time for course ''")
            days = input("Enter days of course ''")
            semester = input("Enter the semester for this course ''")
            year = input("Enter the year for this course ''")
            credits = input("Enter the amount of credits for this course")

            sql_command = """ INSERT INTO COURSE VALUES (""" + title + """,""" + CRN + """,""" + dpt + """,""" + id + """,""" + time + """,""" + days + """,""" + semester + """,""" + year + """,""" + credits + """); """
            print(sql_command)

            database.cursor.execute(sql_command)
            print(title + " Has been successfully added to the database")
            database.commit()
        # connect to database
        # use course,date and time to add a course

    def adminremove(self):
        CRN = input("Enter the CRN for the course you want to remove")
        database.cursor.execute("""SELECT TITLE FROM COURSE WHERE CRN = """+CRN+""" ;""")
        print("Has been removed from database")
        sql_command = """DELETE FROM COURSE WHERE CRN = """+CRN+"""; """
        database.cursor.execute(sql_command)
        sql_command = """DELETE FROM STUDENTCOURSE WHERE CRN = """ + CRN + """; """
        database.cursor.execute(sql_command)
        database.commit()
        # connect to database
        # use course name to delete

    def adminadduser(self, idnum, Fname, Lname):
        pass
        # new user(idum,Fname,Lname

    def adminremoveuser(self, idnum, Fname, Lname):
        pass
        # delete user (idnum,Fname,Lname)

    def adminforceadd(self, course, idnum, Fname, Lname):
        pass
        # connect to database
        # use paramenter to override student

    def adminforceremove(self, course, idnum, Fname, Lname):
        pass
        # connect to database
        # Use parameter to remove student from course

    def searchcourse(self):
        CRN = input("Enter the CRN code of the course you would like to search")
        sql_command = """SELECT 1 FROM COURSE WHERE CRN = """ + CRN + """;"""
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()
        if query_result == []:
            print("The CRN code does not exist")
            return
        else:
            sql_command = """SELECT TITLE FROM COURSE WHERE CRN = """ + CRN + """; """
            database.cursor.execute(sql_command)
            query_result = database.cursor.fetchall()
            for i in query_result:
                print(i)

    def rosterprint(self, course):
        pass
        # pass in course to database
        # print roster array
