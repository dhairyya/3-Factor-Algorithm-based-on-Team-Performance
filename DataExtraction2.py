# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 15:08:46 2018

@author: Dhairyya
"""




import urllib2
from bs4 import BeautifulSoup

url ="http://www.cricbuzz.com/cricket-series/2367/karnataka-premier-league-2015/matches"
page=urllib2.urlopen(url)

soup=BeautifulSoup(page)

#print soup.prettify()
file=open(r'C:\Users\Dhairyya\Desktop\IPL Data\kpl_2015.txt','w')
elems=soup.select(".text-hvr-underline")

#print type(elems)
#print len(elems)
pre="http://www.cricbuzz.com/live-cricket-scorecard"
elems=elems[:-2]


for elem in elems:
    print elem.getText()
    file.write(elem.getText()+'\n\n')
    string=elem.get('href')
    index= string.index('/',1)
    url1=(pre+string[index:])
    
    page1=urllib2.urlopen(url1)
    soup1=BeautifulSoup(page1)
    elems1=soup1.select(".cb-scrd-itms")
    for elem1 in elems1:
        string1=((elem1.getText()).encode("utf-8")).strip()
        if(string1.startswith('Did not')==False and string1.startswith('Extras')==False):
            file.write(string1+"\n")
    file.write('\n')
    
file.close()