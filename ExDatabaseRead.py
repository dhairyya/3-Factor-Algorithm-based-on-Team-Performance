# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 14:46:09 2018

@author: Dhairyya


SQLIte database connection to write
"""
import sqlite3

connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()

sql_command="""DROP TABLE pvalue;"""

crsr.execute(sql_command)

sql_command="""CREATE TABLE pvalue(
entry_number INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50),
value REAL,
matchImp REAL)
;"""

crsr.execute(sql_command)

#sql_command = """INSERT INTO pvalue(name,value,matchImp) VALUES ("Rohit", 24.6, 1.0);"""
#crsr.execute(sql_command)

sql_command = "INSERT INTO pvalue(name, \
       value, matchImp) \
       VALUES ('%s', '%f', '%f' )" % \
       ('Rohit', 25.6,1.0)

crsr.execute(sql_command)
connection.commit()

connection.close()
