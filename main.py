import database
import classes


def login():
    id = input("Enter your id number! or type quit to close program\n")
    if(id == 'quit'):
        exit()
    else:
        checkuser(id)
def logout(user):
    del user
    print("You have been logged out\nreturning to login\n------------\n")
    login()

def checkstudent(id):
    sql_command = """SELECT 1 FROM STUDENT WHERE ID = """ + id + """;"""
    database.cursor.execute(sql_command)
    query_result = database.cursor.fetchall()
    if query_result == []:
        return
    else:
        result = str(query_result[0])
        #print(result)
        return result
def checkinstructor(id):
    sql_command = """SELECT 1 FROM INSTRUCTOR WHERE ID = """ + id + """;"""
    database.cursor.execute(sql_command)
    query_result = database.cursor.fetchall()
    if query_result == []:
        return
    else:
        result = str(query_result[0])
        #print(result)
        return result

def checkadmin(id):
    sql_command = """SELECT 1 FROM ADMIN WHERE ID = """ + id + """;"""
    database.cursor.execute(sql_command)
    query_result = database.cursor.fetchall()
    if query_result == []:
        return
    else:
        result = str(query_result[0])
        #print(result)
        return result

def studentfunctions(student,id):
    while(1):
        choice = input("1 to add a course to your schedule\n2 to remove a course from your schedule\n3 to print out current enrolled course\n4 to search course by CRN\n5 to Drop a course\n6 to print all courses\n0 to logout\n")
        if(choice == '1'):
            student.addCourse(id)
        elif(choice == '2'):
            student.dropCourse(id)
        elif(choice == '3'):
            student.sprint(id)
        elif(choice == '4'):
            student.searchcourse()
        elif(choice == '5'):
            student.dropCourse(id)
        elif(choice == '6'):
            student.print()
        elif(choice == '0'):
            logout(student)
        else:
            print("Invalid input\n")
def instructorfunctions(instructor,id):
    while(1):
        choice = input("1 to print students ID in your class\n2 to search course by CRN\n3 to print out all courses\n0 to logout\n")
        if(choice == '1'):
            instructor.rosterprint(id)
        elif(choice == '2'):
            instructor.searchcourse()
        elif(choice == '3'):
            instructor.print()
        elif(choice == '0'):
            logout(instructor)
def adminfunctions(admin,id):
    while(1):
        choice = input("1 to add a course to the system\n2 to remove a course from the system\n3 to search course by CRN\n4 to print out all courses\n0 to logout\n")
        if(choice == '1'):
            admin.adminadd()
        elif(choice == '2'):
            admin.adminremove()
        elif(choice == '3'):
            admin.searchcourse()
        elif(choice == '4'):
            admin.print()
        if(choice == '0'):
            logout(admin)

def checkuser(id):
    if (checkstudent(id) == '(1,)'):
        print("Welcome Student\n")
        sql_command = """ SELECT NAME,SURNAME FROM STUDENT WHERE ID = """ + id + """;"""
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()
        print(str(query_result))
        print("Here is a list of your functions\n")

        database.cursor.execute("""SELECT * FROM STUDENT WHERE ID = """ + id + """;""")
        query_result = database.cursor.fetchall()

        result = query_result[0]
        ID = result[0]
        Name = result[1]
        Surname = result[2]
        GradYear = result[3]
        Major = result[4]
        Email = result[5]
        student1 = classes.student(ID,Name,Surname,GradYear,Major,Email)
        #call studnet functions
        studentfunctions(student1,ID)


        exit()
    elif(checkinstructor(id) == '(1,)'):
        print("Welcome Instructor")
        sql_command = """ SELECT NAME,SURNAME FROM INSTRUCTOR WHERE ID = """ + id + """;"""
        database.cursor.execute(sql_command)
        query_result = database.cursor.fetchall()
        print(str(query_result))
        print("Here is a list of your functions\n")

        database.cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = """ + id + """;""")
        query_result = database.cursor.fetchall()

        result = query_result[0]
        id = result[0]
        name = result[1]
        surname = result[2]
        title = result[3]
        hireyear = result[4]
        dept = result[5]
        email = result[6]

        instructor1 = classes.instructor(id,name,surname,title,hireyear,dept,email)
        instructorfunctions(instructor1,id)
        exit()
    elif(checkadmin(id) == '(1,)'):
        print("Welcome Admin")
        database.cursor.execute("""SELECT * FROM ADMIN WHERE ID = """ + id + """;""")
        query_result = database.cursor.fetchall()

        result = query_result[0]
        id = result[0]
        name = result[1]
        surname = result[2]
        title = result[3]
        office = result[4]
        email = result[5]

        admin1 = classes.admin(id,name,surname,title,office,email)
        adminfunctions(admin1,id)

        exit()
    else:
        print("My code sucks or your username is invalid")
        login()



login()

database.commit()
database.close()
