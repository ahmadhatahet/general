import sqlite3

# start db in memory
conn = sqlite3.connect(':memory:')

# initiate cusrsor
cursor = conn.cursor()

# creating db
# createdb = 'CREATE DATABASE IF NOT EXISTS family'
# cursor.execute(createdb)

# create table
insterttable = '''CREATE TABLE IF NOT EXISTS members (
    id              INTEGER         PRIMARY KEY AUTOINCREMENT   NOT NULL,
    name            VARCHAR(100)                NOT NULL,
    dob             DATE                        NOT NULL,
    current_state   VARCHAR(255)
)'''
cursor.execute(insterttable)

# cursor.execute('PRAGMA table_info(members)')
# print(cursor.fetchall())
# exit()

# insert values
col = ['name','dob']
insertinto = f'INSERT INTO members ({col[0]}, {col[1]}) values(?, ?)'

values = [
    ('John Doe', '1953-05-20'),
    ('Katja Doe', '1964-10-30'),
    ('Child 1', '1990-10-10'),
    ('Child 2', '1990-10-10'),
    ('Child 3', '1990-10-10')
]

cursor.executemany(insertinto, values)

# cursor.execute('SELECT * from members')
# print(cursor.fetchall())
# exit()

# update records
update_col = 'dob'
setvalues = f'UPDATE members SET {update_col}=? WHERE name=?'
new_values = [
    ('merchant', 'John Doe'),
    ('IT-Administrator', 'Katja Doe'),
    ('Master Student', 'Child 1'),
    ('Product Manager', 'Child 2'),
    ('School Student', 'Child 3')
]
cursor.executemany(setvalues, new_values)


# selectdb = 'USE DATABSE family'
selectquery = 'SELECT * from members'
cursor.execute(selectquery)
result = cursor.fetchone()
while result:
    print(result)
    result = cursor.fetchone()

# closing connenction
conn.close()
exit()