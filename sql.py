import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a curser object to Insert Record, Create Table , Retrive Data
cursor = connection.cursor()


## Create a table 
table_info = """

Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

## Insert some more records

cursor.execute('''Insert into STUDENT values('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('Sudhanshu', 'Data Science', 'B', 100)''')
cursor.execute('''Insert into STUDENT values('Darius', 'Data Science', 'A', 86)''')
cursor.execute('''Insert into STUDENT values('Vikash', 'Devops ', 'A', 50)''')
cursor.execute('''Insert into STUDENT values('Dipesh', 'Devops ', 'A', 35)''')


## Display all the records
print("The Inserted Records are ..")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection
    
connection.commit()
connection.close()