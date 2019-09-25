# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 01:35:50 2019

@author: Apratim
"""

import csv

with open('route.csv','r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        print(lat)
        print(long)
        print(lat+long)