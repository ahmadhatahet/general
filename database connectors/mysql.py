import pyodbc

connection_string = (
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'UID=root;'
    'PWD=root;'
)

myconn = pyodbc.connect(connection_string)
# myconn.autocommit = True

# initiate cursor
c = myconn.cursor()
# c.fast_executemany=True


# creating db
createdb = 'CREATE database if not exists family'
c.execute(createdb)


# delete table if exist to overcome any duplicates
c.execute('DROP TABLE if exists family.members')


# create table
insterttable = '''
CREATE TABLE family.members (
id              INT             PRIMARY KEY     AUTO_INCREMENT  NOT NULL,
name            VARCHAR(100)                                    NOT NULL,
dob             DATE                                            NOT NULL,
current_state   VARCHAR(255)
)
'''
c.execute(insterttable)

# print all columns
c.execute('DESCRIBE family.members')
print(c.fetchall())


# insert values
col = ['name','dob']
insertinto = f'INSERT INTO family.members ({col[0]}, {col[1]}) values(?, ?)'
values = [
    ('John Doe', '1953-05-20'),
    ('Katja Doe', '1964-10-30'),
    ('Child 1', '1990-10-10'),
    ('Child 2', '1990-10-10'),
    ('Child 3', '1990-10-10')
]
c.executemany(insertinto, values)
c.commit()

# Test inserted records
print('-'*50)
c.execute('SELECT * FROM family.members')
print(c.fetchall())


# update records
update_col = 'current_state'
setvalues = f'UPDATE family.members SET {update_col}=? WHERE name=?'
new_values = [
    ('Merchant','John Doe'),
    ('IT-Administrator','Katja Doe'),
    ('Master Student','Child 1'),
    ('Product Manager','Child 2'),
    ('School Student','Child 3')
]
c.executemany(setvalues, new_values)
c.commit()


# Get all data
print('-'*50)
selectquery = 'SELECT * FROM family.members'
c.execute(selectquery)
result = c.fetchone()
while result:
    print(result)
    result = c.fetchone()


# closing connenction
myconn.close()
exit()