# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 13:39:53 2018

@author: Dhairyya
"""

import requests
from bs4 import BeautifulSoup

url ="http://www.iplt20.com/match/2017/60?tab=scorecard"
res=requests.get(url)
res.raise_for_status()


soup=BeautifulSoup(res.text)



elems=soup.select(".batsmanInns")

print type(elems)
print len(elems)

print elems
file=open('C:\Users\Dhairyya\Desktop\data.txt','w')
file.write((res.text).encode('utf-8'))


#for elem in elems:
#    string=((elem.getText()).encode("utf-8")).strip()
#    if(string.startswith('Did not')==False and string.startswith('Extras')==False):
#       file.write(string+"\n")

file.close()

#print string
#print string.startswith('Did not')