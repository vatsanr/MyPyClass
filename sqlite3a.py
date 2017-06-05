import sqlite3

# Opening DB function, given a name
def open_db(name):
    conn=sqlite3.connect(name)
    cur=conn.cursor()
    return conn, cur

#Closing DB function, given a connection
def close_db(conn):
    conn.commit()
    conn.close()

#Create a table function, given a connection
def create_table(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS STORE (item TEXT, quantity INTEGER, price REAL)")

# Insert rows into a table function
def insert_rows(cur,item,quantity,price):
    cur.execute("INSERT INTO STORE VALUES(?,?,?)",(item,quantity,price))

# delete all rows
def delete_rows(cur):
    cur.execute("DELETE FROM STORE")

def delete_row(cur,item):
    cur.execute("DELETE FROM STORE WHERE item=?",(item,))


# View all rows in the table function
def view_all(cur):
    cur.execute("SELECT * FROM STORE")
    rows=cur.fetchall()
    print(rows)

#Open DB
conn, cur = open_db("lite.db")
create_table(cur)
close_db(conn)

# Insert Rows
conn, cur = open_db("lite.db")
delete_rows(cur)
insert_rows(cur,"Water Glass",5,10.5)
insert_rows(cur,"Wine Glass",10,20.0)
insert_rows(cur,"Coffee Cup",8,6.5)
delete_row(cur,"Wine Glass")

# Print all Rows
view_all(cur)
#Close DB
close_db(conn)
