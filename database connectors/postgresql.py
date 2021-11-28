import psycopg2

myconn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="root"
)

# initiate cursor
c = myconn.cursor()


# check if db is already exists
c.execute("SELECT * FROM pg_database WHERE datname = 'family'")
is_db = c.fetchall() == []

# creating db if not
c.execute('''
CREATE DATABASE family
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'German_Germany.utf8'
    LC_CTYPE = 'German_Germany.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
''')

# create table
insterttable = '''
CREATE TABLE members (
id              INT             PRIMARY KEY     AUTOINCREMENT   NOT NULL,
name            VARCHAR(100)                                    NOT NULL,
dob             DATE                                            NOT NULL,
current_state   VARCHAR(255)
)
'''
c.execute(insterttable)

# print all columns
c.execute("SELECT * FROM information_schema.columns WHERE table_name='members'")
print(c.fetchall())


# insert values
col = ['name', 'dob']
insertinto = f'INSERT INTO members ({col[0]}, {col[1]}) values(?, ?)'
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
c.execute('SELECT * FROM members')
print(c.fetchall())


# update records
update_col = 'current_state'
setvalues = f'UPDATE members SET {update_col}=? WHERE name=?'
new_values = [
    ('Merchant', 'John Doe'),
    ('IT-Administrator', 'Katja Doe'),
    ('Master Student', 'Child 1'),
    ('Product Manager', 'Child 2'),
    ('School Student', 'Child 3')
]
c.executemany(setvalues, new_values)
c.commit()


# Get all data
print('-'*50)
selectquery = 'SELECT * FROM members'
c.execute(selectquery)
result = c.fetchone()
while result:
    print(result)
    result = c.fetchone()


# closing connenction
myconn.close()
exit()
