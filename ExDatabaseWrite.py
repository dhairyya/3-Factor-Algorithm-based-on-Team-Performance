# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 15:00:17 2018

@author: Dhairyya

SQLIte database connection to read
"""

import sqlite3
import matplotlib.pyplot as plt

connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()

#crsr.execute("SELECT Distinct name from  pvalue WHERE name=?",("Rohit Sharma",))
crsr.execute("SELECT DISTINCT name from fieldValue")
#crsr.execute("SELECT DISTINCT name from IPLFieldValue2018")

data=crsr.fetchall()
players=[]
p=[]
value=[]

for row in data:
    name = row[0].encode("ascii")
    players.append(name)


for player in players:
    crsr.execute("SELECT * from  fieldValue WHERE name=?",(player,))
    #crsr.execute("SELECT * from  IPLFieldValue2018 WHERE name=?",(player,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
        total=total+(row[2]*row[4])
#        total=total+(row[2]*row[3])
    p.append(player)
    value.append(total)


xaxis=[]
yaxis=[]    
i=0    
while i<10: 
    mval=max(value)
    pos=value.index(mval)
    if p[pos]!='su' and p[pos]!='&':
        print p[pos]+" "+str(value[pos])
        xaxis.append(value[pos])
        yaxis.append(p[pos])
    if p[pos]=='su' or p[pos]=='&':
        i=i-1
    p.remove(p[pos])
    value.remove(value[pos])
    i=i+1


plt.plot(xaxis,yaxis,color="green",linestyle="dashed",linewidth=1,marker='o',markerfacecolor='red',markersize=5)
plt.ylabel('player name')
plt.xlabel('fielding value')
plt.title('Fielding value of player IPL 2017 & 2016')
plt.show()