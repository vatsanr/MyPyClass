import sqlite3

class Database():
    def __init__(self):
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year NUMBER, isbn NUMBER)")
        self.conn.commit()

    def insert(self,title="",author="",year="",isbn=""):
        self.cur.execute("INSERT into book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def viewAll(self):
        self.cur.execute("SELECT * from book")
        rows=self.cur.fetchall()
        return rows

    def delete(self,id=""):
        self.cur.execute("DELETE from book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("Update book SET title=?, author=?, year=?,isbn=? where id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("Select * from book WHERE (title=? OR author=? or year=? or isbn=?)",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows
    def __del__(self):
        self.conn.close()

#insert("Amazon","Higley",1998,1929222)
#delete("2")
#print(viewAll())
#print(search(author="Trump"))
