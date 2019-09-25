# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:28:18 2019

@author: Apratim
"""

def bubble(a):
    n = len(a)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                temp= a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                
a = [5,1,4,2,8]
bubble(a)

for i in a:
    print(i)                