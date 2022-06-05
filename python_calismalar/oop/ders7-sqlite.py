#baya database systems dersi gibi

import sqlite3
from sqlite3.dbapi2 import connect

def selectOperasyonlari():
    connection = sqlite3.connect("/Users/dejkoveci/Documents/Çalışmalarım/python çalışmalar/oop/chinook.db")

    # cursor = connection.execute("""select FirstName,LastName
    #                              from customers
    #                              where city ='Prague' or city='Berlin'
    #                              order by FirstName,LastName desc""")
    # for row in cursor:
    #     print("First Name = " + row[0])
    #     print("Last Name = " + row[1])
    #     print("***********")

    # cursor = connection.execute("""select city,count(*) from Customers
    #                              group by city having count(*)>1
    #                             order by count(*) desc""")

    # for row in cursor:
    #     print("City = " + row[0])
    #     print("Count = " + str(row[1]))
    #     print("***********")

    cursor = connection.execute("""select FirstName,LastName
                                from customers
                                where FirstName like '%ja' """)
    for row in cursor:
        print("First Name = " + row[0])
        print("Last Name = " + row[1])
        print("***********")

    connection.close()

selectOperasyonlari()

def insertCustomer():
    connection = sqlite3.connect("/Users/dejkoveci/Documents/Çalışmalarım/python çalışmalar/oop/chinook.db")
    connection.execute("""insert into customers
                        (firstName,lastName,city,email)
                        values('Furkan','Çalışkan','Karabük','sad23@sad.com') """)
    connection.commit()
    connection.close()

# insertCustomer()

def updateCustomer():
    connection = sqlite3.connect("/Users/dejkoveci/Documents/Çalışmalarım/python çalışmalar/oop/chinook.db")
    connection.execute("""update customers set city= 'İstanbul'
                        where city='Karabük' """)
    connection.commit()
    connection.close()

# updateCustomer()

def deleteCustomer():
    connection = sqlite3.connect("/Users/dejkoveci/Documents/Çalışmalarım/python çalışmalar/oop/chinook.db")
    connection.execute("""delete from customers
                        where customerid= 60 """)
    connection.commit()
    connection.close()

# deleteCustomer()

def joinOperasyonları():
    connection = sqlite3.connect("/Users/dejkoveci/Documents/Çalışmalarım/python çalışmalar/oop/chinook.db")
    cursor = connection.execute("""SELECT albums.Title,
                                 artists.Name FROM artists inner join  albums
                                on artists.ArtistId = albums.AlbumId """)

    for row in cursor:
        print("Title = " +  row[0] + "Name = " +  row[1])
      
    
    connection.close()

joinOperasyonları()