# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:31:36 2018

@author: Dhairyya
"""

from selenium import webdriver
import sqlite3
import time

number=60
url='http://www.iplt20.com/match/2016/'+str(number)+'?tab=scorecard'

browser=webdriver.Chrome(executable_path=r'C:\Users\Dhairyya\Downloads\chromedriver_win32\chromedriver.exe')
browser.get(url)

time.sleep(3)


#######################################################################
connection=sqlite3.connect("myTable.db")

crsr=connection.cursor()
#######################################################################

teamScorecard=browser.find_elements_by_class_name('teamScorecard')

for score_elem in teamScorecard:
    batsmen=score_elem.find_element_by_class_name('batsmen')
    bat_player=batsmen.find_elements_by_class_name('player-popup-link')
    for batter in bat_player:
       text=(batter.find_element_by_class_name('dismissal')).text
       text=(text.encode("utf-8")).strip()
       if text=="NOT OUT":
           continue
       else:
           if text.startswith('c&')==True or text.startswith('c &'):
               continue
           if text.startswith('c ')==True:
               pos=text.index('b ',2)
               print text[2:pos].strip()
               sql_command = "INSERT INTO fieldValue(name, \
               value, year, matchImp) \
               VALUES ('%s', '%f', '%d', '%f' )" % \
               (text[2:pos].strip(),1.0,2016,2.00)
               crsr.execute(sql_command)
               
           if text.startswith('st ')==True:
               pos=text.index('b ',3)
               print text[3:pos].strip()
               sql_command = "INSERT INTO fieldValue(name, \
               value,year, matchImp) \
               VALUES ('%s', '%f', '%d','%f' )" % \
               (text[3:pos].strip(),1.0,2016,2.00)
               crsr.execute(sql_command)
           
           if text.startswith('run out ')==True:
                pos=text.index('(')
                fin=text.index(')')
                print text[(pos+1):fin].strip()
                sql_command = "INSERT INTO fieldValue(name, \
                value, year, matchImp) \
                VALUES ('%s', '%f', '%d', '%f' )" % \
                (text[(pos+1):fin].strip(),1.0,2016,2.00)
                crsr.execute(sql_command)
    
print "Done"
connection.commit()
connection.close()