# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:40:48 2019

@author: Apratim
"""
from statistics import mean
from scipy import stats
Estimates = [1000,10101,1786,2000,1500,1500,100,120,150,150,170,175,180,197,200,200,200,200,200,200,200,220,220,200,220,234,250,250,250,250,250,250,250,250,263,270,275,275,275,286,300,300,300,300,300,300,300,300,320,350,350,400,400,400,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,728]
Estimates.sort()
m = stats.trim_mean(Estimates,0.1)
print(m)
#tv=int(0.1*len(Estimates))
#Estimates=Estimates[tv:]
#Estimates=Estimates[:len(Estimates)-tv]
#print (mean(Estimates))
#or i in range(len(Estimates)):
    #print(Estimates[i])