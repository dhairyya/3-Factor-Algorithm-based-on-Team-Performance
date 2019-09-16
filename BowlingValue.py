# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:36:47 2018

@author: Dhairyya
"""

from selenium import webdriver
import sqlite3
import time
import sys


connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()


number=1
url='http://www.iplt20.com/match/2016/0'+str(number)+'?tab=scorecard'

browser=webdriver.Chrome(executable_path=r'C:\Users\Dhairyya\Downloads\chromedriver_win32\chromedriver.exe')
browser.get(url)

time.sleep(3)


teamScorecard=browser.find_elements_by_class_name('teamScorecard')
bowl_name=[]#done
wicketsTakenByTeam=[]#done
runsGivenByTeam=[]#done
wicketsTakenByBowler=[]#done
runsGivenByBowler=[]#done
oversThrownByBowler=[]#done
noBowler=[]#done




for score_elem in teamScorecard:
    batsmen=score_elem.find_element_by_class_name('batsmen')
    total=(batsmen.find_element_by_class_name('total')).find_element_by_class_name('runs')
    w=(batsmen.find_element_by_class_name('total')).find_element_by_class_name('info')
    w=w.text
    w=w.encode('utf-8')
    index = w.index(';')
    w = w[1:index]
    if w=="All out":
        w=11
    else:
        w=int(w[0:1])+2
    runsGivenByTeam.append(total.text)
    wicketsTakenByTeam.append(w)
    bowlers=score_elem.find_element_by_class_name('bowlers')
    bowl_player=bowlers.find_elements_by_class_name('player-popup-link')
    noBowler.append(len(bowl_player))
    for bowler in bowl_player:
        bowl_name.append((bowler.find_element_by_class_name('player')).text)
        data=bowler.find_elements_by_tag_name('td')
        data=data[2:5]
        oversThrownByBowler.append(data[0].text)
        runsGivenByBowler.append(data[1].text)
        wicketsTakenByBowler.append(data[2].text)
##########################################################################################
        
#print noBowler
#print runsGivenByTeam
#print wicketsTakenByTeam
#print bowl_name
#print oversThrownByBowler
#print runsGivenByBowler
#print wicketsTakenByBowler
#############################################################################################
        
#innings2 bowling
for i in range(0,noBowler[0]):
    if float(wicketsTakenByTeam[0])==0.0:
        v1=sys.float_info.max
    else:
        v1=float(runsGivenByTeam[0])/float(wicketsTakenByTeam[0])
        
    if float(wicketsTakenByBowler[i])==0.0:
        v2=sys.float_info.max
    else:
        v2=float(runsGivenByBowler[i])/float(wicketsTakenByBowler[i])
        
    if float(runsGivenByBowler[i])==0.0:
            v3=sys.float_info.max
    else:
            v3=float(runsGivenByBowler[i])/float(oversThrownByBowler[i])
        
    value1=(float(wicketsTakenByBowler[i])*v1)-float(runsGivenByBowler[i])
    bowlingValue=value1/(v2*v3)
    print bowl_name[i]+" "+str(bowlingValue)
    sql_command = "INSERT INTO bowlValue(name, \
    value, year, matchImp) \
    VALUES ('%s', '%f', '%d','%f' )" % \
    (bowl_name[i], bowlingValue,2016,1.0)
    crsr.execute(sql_command)
    

#innings1 bowling
for i in range(noBowler[0],noBowler[0]+noBowler[1]):
    if float(wicketsTakenByTeam[1])==0.0:
        v1=sys.float_info.max
    else:
        v1=float(runsGivenByTeam[1])/float(wicketsTakenByTeam[1])
    
    if float(wicketsTakenByBowler[i])==0.0:
        v2=sys.float_info.max
    else:
        v2=float(runsGivenByBowler[i])/float(wicketsTakenByBowler[i])
        
    if float(runsGivenByBowler[i])==0.0:
            v3=sys.float_info.max
    else:
            v3=float(runsGivenByBowler[i])/float(oversThrownByBowler[i])

    value1=(float(wicketsTakenByBowler[i])*v1)-float(runsGivenByBowler[i])
    bowlingValue=(value1/(v2*v3))
    print bowl_name[i]+" "+str(bowlingValue)
    sql_command = "INSERT INTO bowlValue(name, \
    value, year, matchImp) \
    VALUES ('%s', '%f', '%d','%f' )" % \
    (bowl_name[i], bowlingValue,2016,1.0)
    crsr.execute(sql_command)
    
print "done"
connection.commit()
connection.close()