import sqlite3

## connect to sql
connection = sqlite3.connect("student.db")
## create a cursor to insert , udpate , select
cursor = connection.cursor()
## create table
table_info = """create table STUDENT(NAME VARCHAR(50), CLASS VARCHAR(50), SECTION VARCHAR(10),MARKS INT);"""
cursor.execute(table_info)
## insert records
cursor.execute('''Insert Into STUDENT values('Arun','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Rahul','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Rajesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Omar','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('John','DEVOPS','A',35)''')
## Display
print("inserted records are")
data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
cursor.close()

