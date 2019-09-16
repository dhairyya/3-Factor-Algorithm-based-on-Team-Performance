# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:07:17 2018

@author: Dhairyya
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:24:39 2018

@author: Dhairyya
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:20:51 2018

@author: Dhairyya
"""

import sqlite3

connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()

playersTeam1=['David Warner','Shikhar Dhawan','Moises Henriques','Yuvraj Singh','Deepak Hooda','Ben Cutting','Naman Ojha','Bipul Sharma','Bhuvneshwar Kumar','Barinder Sran','Mustafizur Rahman']
playersTeam2=['Chris Gayle','Virat Kohli','AB de Villiers','Lokesh Rahul','Shane Watson','Sachin Baby','Stuart Binny','Chris Jordan','Iqbal Abdulla','Yuzvendra Chahal','Sreenath Arvind']

sumTotalBatTeam1=0
sumTotalBowlTeam1=0
sumTotalFieldTeam1=0
sumTotalTeam1=0

#batting team1
for player in playersTeam1:
    crsr.execute("SELECT * from  batValue WHERE name=? and year=2016",(player,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    if count==0:
        count=1
    total=total/count
    sumTotalBatTeam1=sumTotalBatTeam1+total

#bowling team1
for player in playersTeam1:
    crsr.execute("SELECT * from  bowlValue WHERE name=? and year=2016",(player,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    if count==0:
        count=1
    total=total/count
    sumTotalBowlTeam1=sumTotalBowlTeam1+total    

#fielding team1
for player in playersTeam1:
    crsr.execute("SELECT * from  fieldValue WHERE name=? and year=2016",(player,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    if count==0:
        count=1
    total=total/count
    sumTotalFieldTeam1=sumTotalFieldTeam1+total
    
sumTotalTeam1 = sumTotalBatTeam1 + sumTotalBowlTeam1 + sumTotalFieldTeam1

#############################################################################
#team2
############################################################################

sumTotalBatTeam2=0
sumTotalBowlTeam2=0
sumTotalFieldTeam2=0
sumTotalTeam2=0

#batting team2
for player in playersTeam2:
    crsr.execute("SELECT * from  batValue WHERE name=? and year=2016",(player,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    if count==0:
        count=1
    total=total/count
    sumTotalBatTeam2=sumTotalBatTeam2+total

#bowling team2
for player in playersTeam2:
    crsr.execute("SELECT * from  bowlValue WHERE name=? and year=2016",(player,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    if count==0:
        count=1
    total=total/count
    sumTotalBowlTeam2=sumTotalBowlTeam2+total 
    
#fielding team2
for player in playersTeam2:
    crsr.execute("SELECT * from  fieldValue WHERE name=? and year=2016",(player,))
    data=crsr.fetchall()
    total=0
    count=0
    for row in data:
       total=total+(row[2]*row[4])
       count=count+row[4]
    if count==0:
        count=1
    total=total/count
    sumTotalFieldTeam2=sumTotalFieldTeam2+total
    

sumTotalTeam2 = sumTotalBatTeam2 + sumTotalBowlTeam2 + sumTotalFieldTeam2

print "\n"

print "Sunrisers Hyderabad Batting Score is "+str(sumTotalBatTeam1)
print "Royal Challengers Bangalore Batting Score is "+str(sumTotalBatTeam2)
if sumTotalBatTeam1>sumTotalBatTeam2:
    print "Sunrisers Hyderabad is superior in batting department\n"
else:
    print "Royal Challengers Bangalore is superior in batting department\n"

print "Sunrisers Hyderabad Bowling Score is "+str(sumTotalBowlTeam1)
print "Royal Challengers Bangalore Bowling Score is "+str(sumTotalBowlTeam2)
if sumTotalBowlTeam1>sumTotalBowlTeam2:
    print "Sunrisers Hyderabad is superior in bowling department\n"
else:
    print "Royal Challengers Bangalore is superior in bowling department\n"


print "Sunrisers Hyderabad Fielding Score is "+str(sumTotalFieldTeam1)
print "Royal Challengers Bangalore Fielding Score is "+str(sumTotalFieldTeam2)
if sumTotalFieldTeam1>sumTotalFieldTeam2:
    print "Sunrisers Hyderabad is superior in fielding department\n"
elif sumTotalFieldTeam1<sumTotalFieldTeam2 :
    print "Royal Challengers Bangalore is superior in fielding department\n"
else:
    print "Both teams are equal in this aspect\n"
    

print "Sunrisers Hyderabad team score is "+ str(sumTotalTeam1)
print "Royal Challengers Bangalore team score is "+ str(sumTotalTeam2)
print "Diff is "+ str(sumTotalTeam1-sumTotalTeam2) 
if sumTotalTeam1>sumTotalTeam2:
    print "Sunrisers Hyderabad is superior\n"
elif sumTotalTeam1<sumTotalTeam2:
    print "Royal Challengers Bangalore is superior\n"
else:
    print "Both teams are equal in this aspect\n"

print "So Sunrisers Hyderabad Won IPL 2016"
   

