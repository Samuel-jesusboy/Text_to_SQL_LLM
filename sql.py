import sqlite3

#connect to sqlite
connection = sqlite3.connect('Student.db')

#creaate a cursor object to insert records, create tables amd retrive data 
cursor = connection.cursor()

# create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25),
MARKS INT);
"""

cursor.execute(table_info)
#insert some records 

cursor.execute('''INSERT INTO STUDENT VALUES ('Tosin', 'Data Science', 'A', '90')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Ayo', 'Data Science', 'B', '86')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Tolu', 'Devops', 'C', '50')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Emma', 'Data Science', 'C', '52')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Samuel', 'Devops', 'A', '93')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('tim', 'Devops', 'B', '81')''')

# Display all records
print('The following Records were inserted: ')

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)


#close the connection
connection.commit()
connection.close()