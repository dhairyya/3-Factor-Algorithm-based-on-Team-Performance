# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 11:01:13 2018

@author: Dhairyya
"""

from pycricbuzz import Cricbuzz
import sys
import sqlite3

c=Cricbuzz()
matches=c.matches()

match=matches[1]
scorecard=c.scorecard(match['id'])
data=scorecard['scorecard']
#################################################################
connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()
###################################################################


#####################################################################
#Bowling
#####################################################################
for i in range(0,2):
    wicketsTakenByTeam=float(data[i]['wickets'])
    runsGivenByTeam=float(data[i]['runs'])
    bowlingData=data[i]['bowlcard']
    for bowlingFigure in bowlingData:
        bowlerName=bowlingFigure['name'].strip()
        wicketsTakenByBowler=float(bowlingFigure['wickets'])
        runsGivenByBowler=float(bowlingFigure['runs'])
        oversThrownByBowler=float(bowlingFigure['overs'])
        
        if wicketsTakenByTeam==0:
            f1=sys.float_info.max
        else:
            f1=(runsGivenByTeam/wicketsTakenByTeam)
        
        if wicketsTakenByBowler==0:
            f2=sys.float_info.max
        else:
            f2=(runsGivenByBowler/wicketsTakenByBowler)
            
        if runsGivenByBowler==0:
            f3=sys.float_info.max
        else:
            f3=(runsGivenByBowler/oversThrownByBowler)
            
        bowlingValue=((wicketsTakenByBowler*f1)-runsGivenByBowler)/(f2*f3)
        print bowlerName+" "+str(bowlingValue)
        
        sql_command = "INSERT INTO IPLBowlValue2018(name, \
        bowlingValue, matchImp) \
        VALUES ('%s', '%f', '%f' )" % \
        (bowlerName, bowlingValue,1.0)
        crsr.execute(sql_command)
   
###########################################################################
#Fielding
############################################################################
for i in range(0,2):
    fieldingData=data[i]['batcard']
    for row in fieldingData:
        fData=row['dismissal']
        fData=fData.encode('utf-8')
        if fData.startswith('c ')==True:
            pos=fData.index('b ',2)
            print fData[2:pos].strip()
            sql_command = "INSERT INTO IPLFieldValue2018(name, \
            fieldingValue, matchImp) \
            VALUES ('%s', '%f', '%f' )" % \
            (fData[2:pos].strip(),1.0,1.0)
            crsr.execute(sql_command)
        
        if fData.startswith('st ')==True:
            pos=fData.index('b ',3)
            print fData[3:pos].strip()
            sql_command = "INSERT INTO IPLFieldValue2018(name, \
            fieldingValue, matchImp) \
            VALUES ('%s', '%f', '%f' )" % \
            (fData[3:pos].strip(),1.0,1.0)
            crsr.execute(sql_command)
        
        if fData.startswith('run out ')==True:
            pos=fData.index('(')
            fin=fData.index(')')
            print fData[(pos+1):fin].strip()
            sql_command = "INSERT INTO IPLFieldValue2018(name, \
            fieldingValue, matchImp) \
            VALUES ('%s', '%f', '%f' )" % \
            (fData[(pos+1):fin].strip(),1.0,1.0)
            crsr.execute(sql_command)
        
        
        


#####################################################################################
#Batting
#####################################################################################
for i in range(0,2):
    battingData=data[i]['batcard']
    totalBoundaries=0.0
    teamScore=float(data[i]['runs'])
    batsmanPlayed=float(data[i]['wickets'])
    if batsmanPlayed<10.0:
        batsmanPlayed=batsmanPlayed+2.0
    else:
        batsmanPlayed=11.0

    for batsman in battingData:
        boundaries=float(batsman['fours'])+float(batsman['six'])
        totalBoundaries=totalBoundaries+boundaries
    
    for batsman in battingData:
        batsmanName=batsman['name'].strip()
        batsmanRuns=float(batsman['runs'])
        boundaries=float(batsman['fours'])+float(batsman['six'])
    
        ballsFaced=float(batsman['balls'])
        if ballsFaced==0:
            f1=0.0
        else:
            f1=(batsmanRuns/(ballsFaced*10))
    
        dismissal=batsman['dismissal']
        dismissal=dismissal.encode('utf-8')
        if dismissal=="not out":
            outStatus=0.0
        else:
            outStatus=1.0

        battingValue=(batsmanRuns-(outStatus*(teamScore/batsmanPlayed)))+(boundaries/totalBoundaries)+f1
        print batsmanName+" "+str(battingValue)
        
        sql_command = "INSERT INTO IPLBatValue2018(name, \
        battingValue, matchImp) \
        VALUES ('%s', '%f', '%f' )" % \
        (batsmanName, battingValue,1.0)
        crsr.execute(sql_command)
        
##############################################################################3
print "Done"        
connection.commit()
connection.close()