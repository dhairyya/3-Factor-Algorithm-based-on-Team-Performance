# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 13:38:11 2018

@author: Dhairyya
"""

###############################################################################
#Importing library
##############################################################################
from selenium import webdriver
import sqlite3


#############################################################################
#Scraping
############################################################################
number=01
url='http://www.iplt20.com/match/2017/0'+str(01)+'?tab=scorecard'

browser=webdriver.Chrome(executable_path=r'C:\Users\Dhairyya\Downloads\chromedriver_win32\chromedriver.exe')
browser.get(url)
#file=open(r'C:\Users\Dhairyya\Desktop\data.txt','w')
#file.write(str(number))
teamScorecard=browser.find_elements_by_class_name('teamScorecard')
bat_name=[]
bat_status=[]
bat_runs=[]
bat_balls=[]
bat_boundaries=[]
bat_total_boundaries=[]
#bowl=[]
totallist=[]
nobatsman=[]
#nobowler=[]


for score_elem in teamScorecard:
    batsmen=score_elem.find_element_by_class_name('batsmen')
    bat_player=batsmen.find_elements_by_class_name('player-popup-link')
    totalboundaries=0
    nobatsman.append(len(bat_player))
    for batter in bat_player:
        bat_name.append((batter.find_element_by_class_name('player')).text)
        dismissal=(batter.find_element_by_class_name('dismissal')).text
        if(dismissal.find('NOT OUT')>=0):
            bat_status.append(0)
        else:
            bat_status.append(1)
        bat_runs.append((batter.find_element_by_class_name('runs')).text)
        bat_balls.append((batter.find_element_by_class_name('balls')).text)
        fours=(batter.find_element_by_class_name('fours')).text
        sixes=(batter.find_element_by_class_name('sixes')).text
        boundaries=int(fours)+int(sixes)
        bat_boundaries.append(boundaries)
        totalboundaries=totalboundaries+boundaries
#       file.write(name+" "+dismissal+" "+runs+" "+balls+" "+str(boundaries)+" "+str(status))
    bat_total_boundaries.append(totalboundaries)
    total=(batsmen.find_element_by_class_name('total')).find_element_by_class_name('runs')
    total=total.text
    totallist.append(total)
    '''bowler=score_elem.find_element_by_class_name('bowlers')
    bowl_player=bowler.find_elements_by_class_name('player-popup-link')
    nobowler.append(len(bowl_player))
    for bowler in bowl_player:
        bowl.append(bowler.text)'''


#####################################################################
#Scraping complete
########################################################################


        
print bat_name
#print bat_status
#print bat_runs
#print bat_balls
#print bat_boundaries
#print bat_total_boundaries
#print bowl
#print totallist
print nobatsman
#print nobowler    


#####################################################################
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
#########################################################################



#innings 1 batting
for i in range(0,nobatsman[0]):
    value1=(float(bat_runs[i])-((float(bat_status[i]))*(float(totallist[0])/float(nobatsman[0]))))
    value2=(float(bat_boundaries[i])/float(bat_total_boundaries[0]))
    value3=(float(bat_runs[i])/(float(bat_balls[i])*10))
    value=value1+value2+value3
    print bat_name[i]+" "+str(value)
    sql_command = "INSERT INTO pvalue(name, \
       value, matchImp) \
       VALUES ('%s', '%f', '%f' )" % \
       (bat_name[i], float(str(value)),1.0)
    crsr.execute(sql_command)
    
#innings 2 batting
for i in range(nobatsman[0],nobatsman[0]+nobatsman[1]):
    value1=(float(bat_runs[i])-((float(bat_status[i]))*(float(totallist[1])/float(nobatsman[1]))))
    value2=(float(bat_boundaries[i])/float(bat_total_boundaries[1]))
    value3=(float(bat_runs[i])/(float(bat_balls[i])*10))
    value=value1+value2+value3
    print bat_name[i]+" "+str(value)
    sql_command = "INSERT INTO pvalue(name, \
       value, matchImp) \
       VALUES ('%s', '%f', '%f' )" % \
       (bat_name[i], float(str(value)),1.0)
    crsr.execute(sql_command)
    

connection.commit()

connection.close()    