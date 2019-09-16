# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 10:55:32 2018

@author: Dhairyya
"""

import sqlite3

connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()

#sql_command="""DROP TABLE batvalue"""

sql_command="""CREATE TABLE batValue(
entry_number INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50),
value REAL,
year INT,
matchImp REAL)
;"""

crsr.execute(sql_command)


connection.commit()

connection.close()


print "done"