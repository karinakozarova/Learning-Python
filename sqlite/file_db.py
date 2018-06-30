import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()


# c.execute(""" CREATE TABLE User(
#     fname text,
#     lname text
# )""")

c.execute("insert into user values('Karina','Kozarova')")
c.execute("select * from user")

while True:
    res = c.fetchone()
    if res is None:
        break
    else:
         print(res)

conn.commit()
conn.close()