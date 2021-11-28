import pyodbc

# connect to sql server
server = 'AHMAD-YOGA\\SQLEXPRESS'
mydb = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server}'
    + ';SERVER='+ server
    + ';Trusted_Connection=yes'
    + ';fast_executemany = True'
)

# autocommit to enable sql server to excute CREATE DATABASE
# adding autocommit in the connection string didn't work for me
mydb.autocommit = True

# initiate cursor
c = mydb.cursor()

# check sql server version
c.execute("SELECT @@version;")
# testing how fetch only some rows in order to not exhaust the memory
d = c.fetchone()
print('-'*50)
while d:
    print(d[0])
    d = c.fetchone()
# exit()


# creating db
createdb = '''
if not exists(select * from sys.databases where name = 'family')
    begin
        create database family
    end
'''
c.execute(createdb)

# select database
c.execute('USE family')

# create table
insterttable = '''
IF OBJECT_ID('members', 'U') IS NULL
begin
    CREATE TABLE members (
    id              INT             PRIMARY KEY     IDENTITY(1,1)   NOT NULL,
    name            VARCHAR(100)                                    NOT NULL,
    dob             DATE                                            NOT NULL,
    current_state   VARCHAR(255)
    )
end
'''
c.execute(insterttable)

# print all columns
c.execute('''
SELECT
    COLUMN_NAME
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'members'
''')

print(c.fetchall())
# exit()

# insert values
col = ['name','dob']
maxid = 'select max(id) from members'
if [*c.execute(maxid)][0][0] == None:
    insertinto = f'INSERT INTO members ({col[0]}, {col[1]}) values(?, ?)'

    values = [
        ('John Doe', '1953-05-20'),
        ('Katja Doe', '1964-10-30'),
        ('Child 1', '1990-10-10'),
        ('Child 2', '1990-10-10'),
        ('Child 3', '1990-10-10')
    ]

    c.executemany(insertinto, values)

    # Test inserted records
    print('-'*50)
    c.execute('SELECT * from members')
    print(c.fetchall())
    # exit()


# update records
update_col = 'current_state'
setvalues = f'UPDATE members SET {update_col}=? WHERE name=?'
new_values = [
    ('Merchant','John Doe'),
    ('IT-Administrator','Katja Doe'),
    ('Master Student','Child 1'),
    ('Product Manager','Child 2'),
    ('School Student','Child 3')
]

c.executemany(setvalues, new_values)

# Get all data
print('-'*50)
selectquery = 'SELECT * from members'
c.execute(selectquery)
result = c.fetchone()
while result:
    print(result)
    result = c.fetchone()


# closing connenction
mydb.close()
exit()