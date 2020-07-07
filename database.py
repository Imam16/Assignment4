import sqlite3

# database file connection
database = sqlite3.connect("assignment5.db")
#def Enter_Query(database, query):
#    cursor.execute(query)
#    database.commit()
#    print("Query has been executed")


# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
cursor = database.cursor()

######################################################################
# SQL command to create a table in the database
#sql_command = """CREATE TABLE STUDENT (
#ID 		INT 	PRIMARY KEY 	NOT NULL,
#NAME		TEXT	NOT NULL,
#SURNAME		TEXT 	NOT NULL,
#GRADYEAR	INT 	NOT NULL,
#MAJOR		CHAR(4) NOT NULL,
#EMAIL		text	NOT NULL)
#;"""

# execute the statement
#cursor.execute(sql_command)
######################################################################
# SQL command to create a table in the database
#sql_command = """CREATE TABLE INSTRUCTOR (
#ID 		INT 	PRIMARY KEY 	NOT NULL,
#NAME		TEXT	NOT NULL,
#SURNAME		TEXT 	NOT NULL,
#TITLE		TEXT 	NOT NULL,
#HIREYEAR	INT 	NOT NULL,
#DEPT		CHAR(4) NOT NULL,
#EMAIL		text	NOT NULL)
#;"""

# execute the statement
#cursor.execute(sql_command)

######################################################################
# SQL command to create a table in the database
#sql_command = """CREATE TABLE ADMIN (
#ID 		INT 	PRIMARY KEY 	NOT NULL,
#NAME		TEXT	NOT NULL,
#SURNAME		TEXT 	NOT NULL,
#TITLE		TEXT 	NOT NULL,
#OFFICE		TEXT 	NOT NULL,
#EMAIL		text	NOT NULL)
#;"""

# execute the statement
#cursor.execute(sql_command)

#sql_command = """CREATE TABLE COURSE (
 #TITLE   TEXT NOT NULL,
 #CRN     INT PRIMARY KEY NOT NULL,
 #DEPARTMENT      CHAR(4) NOT NULL,
 #INSTRUCTORid     INT NOT NULL,
 #TIME            TEXT NOT NULL,
 #DAYS            TEXT NOT NULL,
 #SEMESTER        TEXT NOT NULL,
 #YEAR            TEXT NOT NULL,
 #CREDITS         INT NOT NULL
 #)
 #;"""


#cursor.execute(sql_command)

#sql_command = """CREATE TABLE STUDENTCOURSE (
# STUDENTID   INT PRIMARY KEYNOT NULL,
# CRN     INT NOT NULL
# )
 #;"""


#cursor.execute(sql_command)

# Student list
#cursor.execute("""INSERT INTO STUDENT VALUES(00010001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010002, 'Marie', 'Curie', 1903, 'BSAS', 'curiem');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010003, 'Nikola', 'Tesla', 1878, 'BSEE', 'telsan');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010004, 'Thomas', 'Edison', 1879, 'BSEE', 'notcool');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010005, 'John', 'von Neumann', 1923, 'BSCO', 'vonneumannj');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010006, 'Grace', 'Hopper', 1928, 'BCOS', 'hopperg');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010007, 'Mae', 'Jemison', 1981, 'BSCH', 'jemisonm');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010008, 'Mark', 'Dean', 1979, 'BSCO', 'deanm');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010009, 'Michael', 'Faraday', 1812, 'BSAS', 'faradaym');""")
#cursor.execute("""INSERT INTO STUDENT VALUES(00010010, 'Ada', 'Lovelace', 1832, 'BCOS', 'lovelacea');""")

# Instructor list
#cursor.execute(
#    """INSERT INTO INSTRUCTOR VALUES(00020001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""")
#cursor.execute(
#    """INSERT INTO INSTRUCTOR VALUES(00020002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
#cursor.execute(
#    """INSERT INTO INSTRUCTOR VALUES(00020003, 'Galileo', 'Galilei', 'Full Prof.', 1600, 'BSAS', 'galileig');""")
#cursor.execute(
#    """INSERT INTO INSTRUCTOR VALUES(00020004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""")
#cursor.execute(
#    """INSERT INTO INSTRUCTOR VALUES(00020005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""")
#cursor.execute(
#    """INSERT INTO INSTRUCTOR VALUES(00020006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")

# Admin list
#cursor.execute("""INSERT INTO ADMIN VALUES(00030001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""")
#cursor.execute(
 #   """INSERT INTO ADMIN VALUES(00030002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""")

# Course list
#cursor.execute("""INSERT INTO COURSE VALUES('Programming',00001,'BSCO',00020004,'15:00','MWF','Spring','2020',4);""")
#cursor.execute("""INSERT INTO COURSE VALUES('Thermo',00002,'BSME',00020006,'10:00','WF','Spring','2030',4);""")
#cursor.execute("""INSERT INTO COURSE VALUES('Analog',00003,'BSEE',00020001,'08:00','MW','Summer','1998',4);""")



# QUERY FOR ALL
#print("Entire STUDENTS")
#cursor.execute("""SELECT * FROM STUDENT""")
#query_result = cursor.fetchall()

#for i in query_result:
#    print(i)

# QUERY FOR ALL
#print("Entire INSTRUCTORS")
#cursor.execute("""SELECT * FROM INSTRUCTOR""")
#query_result = cursor.fetchall()

#for i in query_result:
#    print(i)

# QUERY FOR ALL
#print("Entire ADMINS")
#cursor.execute("""SELECT * FROM ADMIN""")
#query_result = cursor.fetchall()

#for i in query_result:
#    print(i)


# QUERY FOR ALL
#print("Entire COURSES")
#cursor.execute("""SELECT * FROM COURSE""")
#query_result = cursor.fetchall()

#for i in query_result:
#    print(i)



# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
database.commit()

# close the connection
#database.close()
def commit():
   database.commit()


def close():
   database.close