Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_012. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_012/
#Coding Guidelines
Write your code in student.py
A Student has name, age, score and student_id attributes, Where student_id uniquely identifies a student object.

Student class has the following methods to create, retrieve, update and delete student data in the database.

get
save
delete
filter
# get:
get method is used to retrieve a student from the database for the give condition.

Database Table
student_id	name	age	score
1	Raj	20	100
2	Vivek	21	90
3	Roshan	19	100
>>> student_object = Student.get(student_id=1)
>>> student_object.student_id
1
>>> student_object.name
Raj
>>> student_object.age
20
>>> student_object.score
100
If there are no results that match the given condition, get() should raise DoesNotExist exception.
>>> student_object = Student.get(student_id=100)
DoesNotExist:
...
If there are more than one student that match the given condition, get() should raise MultipleObjectsReturned exception.
>>> student_object = Student.get(score=100)
MultipleObjectsReturned:
...
# delete():
Used to delete the given object from the database

Database Table

student_id	name	age	score
1	Raj	20	100
2	Vivek	21	90
3	Roshan	19	100
>>> student_object = Student.get(student_id=1)
>>> student_object.delete()
Database Table
student_id	name	age	score
2	Vivek	21	90
3	Roshan	19	100
# save():
save method creates or updates a student object in database
# update
Database Table
student_id	name	age	score
1	Raj	20	100
2	Vivek	21	90
3	Roshan	19	100
>>> student_object = Student.get(student_id=1)
>>> student_object.name = "Suresh"
>>> student_object.save()
Database Table
student_id	name	age	score
1	Suresh	20	100
2	Vivek	21	90
3	Roshan	19	100
If you have noticed name of the entry in student table with student_id=1 is updated.
# create
create method can be used to create a new entry in the database.

>>> student_object = Student(name="Rajini", age=19, score=95)
>>> student_object.save()
Database Table
student_id	name	age	score
1	Suresh	20	100
2	Vivek	21	90
3	Roshan	19	100
4	Rajini	19	95
If you have noticed, a new entry in student table has been created.
Student class for which below methods are to be implemented.

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    ...


Sample python snippets to execute SQL queries.
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

Reference to access sqlite3 database using python.
Note: You can assume that the table is already created with the below schema in students.sqlite3 database.

CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(250),
    age INT,
    score INT
);
Learn defining custom exceptions in Python in this reference

# Task1:
Implement the get method as mentioned in the description for the below given student class.

# Task2:
Implement a save method for Student class in python whose behavior is as mentioned above.

# Task3:
Implement a delete method for Student class in python whose behavior is as mentioned above.
