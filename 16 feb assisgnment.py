# Q1. What is a database? Differentiate between SQL and NoSQL databases.

'''Database is a collection of data which is organised in a sturctured format like rows and column

SQL :- Structured Query language which is use to interect with relational databases and SQL is a tool for organizing , managing and retrieving data from local databases as well as cloud databases
NoSQL :- Not only Structured query language, NoSQL databases are non-tabular databases and it can handle unstructured data in a large a volume'''

# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

'''DDL :- Data Defination Language(DDL) is a set of SQL commands used to create, modify, and delete database structures but not data. 
       These commands are normally not used by a general user, who should be accessing the database via an application 
       There are some DDL commands :-

       1) create(generate a new table)
           Example :-

           CREATE TABLE new_table(student_ID INT , course_name VARCHAR(100) , course_type VARCHAR(100));

       2) drop(used to delete object from database)
           Example :-
            
            DROP TABLE new_table ;

       3) alter(used to alter the structure of the database)
            Example :-

            ALTER TABLE new_table
            ADD Emails VARCHAR(100);

       4) Truncate(The particular data will be deleted but the structure will remain in the memory for further operation)
            Example :-
            
            TRUNCATE TABLE new_table;
       
       '''
    
    # Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

''' DML :- Data Manipulation Language and it is used to store,modify,retrieve,delete and update data in the database
           and there are common statements are:

                  1)select :- retrieve data from database
                          
                          example:-

                          SELECT * FROM new_table;

                
                  2)insert :- insert data into table

                           example:-

                           INSERT INTO new_table(student_ID , course_name , course_type)
                           VALUES(200145 , DATA SCIENCE MASTERS , Self paced)

                  3)update :- update existing data within the table

                           example:-

                           UPDATE new_table
                           SET course_name = 'FULL STACK WEB DEVELOPMENT'
                           where course_name = 'DATA SCIENCE MASTERS'

                  4)delete :- delete all records from a database table
                  
                           example:-

                           DELETE new_table
                           WHERE course_name = 'FULL STACK WEB DEVELOPMENT'
                           AND course_type = 'Self paced'
                  
                  '''


# Q4. What is DQL? Explain SELECT with an example.

'''DQL :- Data query language is used to fetch the data from the database and it uses only one command

      example:-

             SELECT student_name
             FROM new_table
             WHERE age > 18


'''

# Q5. Explain Primary Key and Foreign Key.

''' Primary Key :- primary key constraints uniquely identifies each record in a table
                :- primary key must contain UNIQUE values and cannot contain NULL values and table can have only one primary key
               

    Foreign Key :- Foreign key constraints is used to prevent actions that would destroy link between table
                :- Foreign key is a field in one table that refers to the primary key in another table 

'''

# Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test1")
mydb.close()

'''
cursor() :-

-In SQL, a cursor is a temporary workstation that is allocated by the database server during the execution of a statement.
-It is a database object that allows us to access data of one row at a time. This concept of SQL is useful when the user wants to update the rows of the table one by one.
-The cursor in SQL is the same as the looping technique of other programming languages. The collection of tuples held by the cursor is known as the active set.
-In SQL database systems, users define the cursor using DECLARE statement and take the SELECT statement as the parameter, which helps in returning the set of rows


execute() :- execute command in SQL is used to execute stored procedures and query string in database servers.

'''

# Q7. Give the order of execution of SQL clauses in an SQL query.

'''SELECT -> FROM -> WHERE
'''
