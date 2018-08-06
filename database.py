import sqlite3

db = sqlite3.connect("data.db")

def createtable():
    db.row_factory=sqlite3.Row
    db.execute("create table if not exists Admin(ID integer primary key autoincrement, Name text,Age int)")

def addvalue(name,age):
    db.execute("insert into Admin(Name,Age) values(?,?)",(name,age))
    db.commit()

def getdata():
    cursor =db.execute("select * from Admin")
    for row in cursor:
        print("Name:{},Age:{}".format(row["Name"],row["Age"]))

def deleteitem(name):
    db.row_factory=sqlite3.Row
    db.execute("delete from Admin where Name ='{}'".format(name))
    db.commit()
    print("{} record was deleted".format(name))

def updateitem(name,age):
    db.execute("update Admin set Age=? where Name=?",(age,name))
    db.commit()

def main():
    createtable()
    addvalue("Khalid",12)
    updateitem("Khalid", 30)
    #deleteitem("Hamoud")
    getdata()


if __name__ == '__main__':
    main()
