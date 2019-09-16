# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 10:55:32 2018

@author: Dhairyya
"""

from pycricbuzz import Cricbuzz
import json

c=Cricbuzz()
matches=c.matches()


for match in matches:
    print json.dumps(c.scorecard(match['id']),indent=4)