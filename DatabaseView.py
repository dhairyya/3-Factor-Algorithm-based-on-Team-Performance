# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 14:04:16 2018

@author: Dhairyya
"""

import sqlite3
import time

connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()

crsr.execute("SELECT * from fieldValue where year=2017")


data=crsr.fetchall()

for row in data:
    print row
    time.sleep(1)


"""
Table schema:
    
    IPLBatValue2018:
        entry_number PRIMARY KEY INTEGER AUTOINCREMENT
        name VARCHAR(50)
        battingValue REAL
        matchImp REAL
    
    IPLBowlValue2018:
        entry_number PRIMARY KEY INTEGER AUTOINCREMENT
        name VARCHAR(50)
        bowlingValue REAL
        matchImp REAL
        
    IPLFieldValue2018:
        entry_number PRIMARY KEY INTEGER AUTOINCREMENT
        name VARCHAR(50)
        fieldingValue REAL
        matchImp REAL
    
    batValue: 
        entry_number PRIMARY KEY INTEGER AUTOINCREMENT
        name VARCHAR(50)
        value REAL
        year INT
        matchImp REAL
        
    bowlValue: 
        entry_number PRIMARY KEY INTEGER AUTOINCREMENT
        name VARCHAR(50)
        value REAL
        year INT
        matchImp REAL
        
    fieldValue: 
        entry_number PRIMARY KEY INTEGER AUTOINCREMENT
        name VARCHAR(50)
        value REAL
        year INT
        matchImp REAL
"""