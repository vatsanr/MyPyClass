import sqlite3

def table_create():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year NUMBER, isbn NUMBER)")
    conn.commit()
    conn.close()

def insert(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT into book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def viewAll():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book")
    rows=cur.fetchall()
    return rows

def delete(id=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE from book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("Update book SET title=?, author=?, year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("Select * from book WHERE (title=? OR author=? or year=? or isbn=?)",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

table_create()
insert("Amazon","Higley",1998,1929222)
delete("2")
update(3,"Amzzzz","Trump","2000","22121211")
print(viewAll())
print(search(author="Trump"))
