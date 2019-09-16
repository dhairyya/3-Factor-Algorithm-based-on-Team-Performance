# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 11:13:46 2018

@author: Dhairyya
"""

import matplotlib.pyplot as plt
import csv

players=[]
price=[]

with open(r'C:\Users\Dhairyya\Desktop\IPL Data\example.csv','r')as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        players.append(str(row[0]))
        price.append(int(row[1]))
   
plt.scatter(players,price,marker='*')

plt.xlabel('players')
plt.ylabel('price')
plt.title('Scatter plot')
plt.legend()

plt.show()
     