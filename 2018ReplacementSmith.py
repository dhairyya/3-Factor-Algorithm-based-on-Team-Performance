# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:42:55 2018

@author: Dhairyya
"""


import sqlite3

connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()

#####################################################################
#Calculating player to be replaced value
##########################################################################
player = "Steve Smith"
PlayerBatting=0
PlayerBowling=0
PlayerFielding=0
PlayerTotal=0

crsr.execute("SELECT * from  batValue WHERE name=?",(player,))
data=crsr.fetchall()
total=0
count=0
for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
if count==0:
        count=1
total=total/count
PlayerBatting=PlayerBatting+total


crsr.execute("SELECT * from  bowlValue WHERE name=?",(player,))
data=crsr.fetchall()
total=0
count=0
for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
if count==0:
        count=1
total=total/count
PlayerBowling=PlayerBowling+total

crsr.execute("SELECT * from  fieldValue WHERE name=?",(player,))
data=crsr.fetchall()
total=0
count=0
for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
if count==0:
        count=1
total=total/count
PlayerFielding=PlayerFielding+total

PlayerTotal = PlayerBatting + PlayerBowling + PlayerFielding

print "\n"
print player +" batting value is "+str(PlayerBatting)+" \n"
print player +" bowling value is "+str(PlayerBowling)+" \n"
print player +" fielding value is "+str(PlayerFielding)+" \n"
print player+" total value is "+ str(PlayerTotal)+" \n"


###########################################################################
#Calculating other player value
############################################################################

#bowling
crsr.execute("SELECT DISTINCT name from bowlValue")

data=crsr.fetchall()
players=[]
pBowling=[]
valueBowling=[]

for row in data:
    name = row[0].encode("ascii")
    players.append(name)


for p in players:
    crsr.execute("SELECT * from  bowlValue WHERE name=?",(p,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    pBowling.append(p)
    valueBowling.append(total/count)

#batting
crsr.execute("SELECT DISTINCT name from batValue")

data=crsr.fetchall()
players=[]
pBatting=[]
valueBatting=[]

for row in data:
    name = row[0].encode("ascii")
    players.append(name)


for p in players:
    crsr.execute("SELECT * from  batValue WHERE name=?",(p,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    pBatting.append(p)
    valueBatting.append(total/count)

#fielding
crsr.execute("SELECT DISTINCT name from fieldValue")

data=crsr.fetchall()
players=[]
pFielding=[]
valueFielding=[]

for row in data:
    name = row[0].encode("ascii")
    players.append(name)


for p in players:
    crsr.execute("SELECT * from  fieldValue WHERE name=?",(p,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    pFielding.append(p)
    valueFielding.append(total/count)
    
################################################################
#Comparing with others
################################################################
print "\nPlayers that can replace "+ player +" are:"
for i in valueBatting:
    if abs(i-PlayerBatting)<3:
        name = pBatting[valueBatting.index(i)]
        if name!=player:
            print name
        