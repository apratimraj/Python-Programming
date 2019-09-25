# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 01:27:46 2019

@author: Apratim
"""
import random
def evolve(x):
    ind = random.randint(0,len(x)-1)
    p = random.randint(1,100)
    print (p)
    if (p==1):
        if(x[ind]=='0'):
            x[ind]=='1'
        else:
            x[ind]=='0'

with open("dna_test.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,10000):
    evolve(x)
print (x)
# 1 is found then change is take place otherwise the change is not take place