# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 01:00:08 2019

@author: Apratim
"""

def binary_search(a, x):
    first_pos = 0
    last_pos = len(a)-1
    flag = 0      #flag=0 means that the element has not been found yet
    
    count =0
    
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid = (first_pos+last_pos)//2
        if(x==a[mid]):
            flag = 1
            print("The element is present"+str(mid))
            print("The number of iterations are:"+str(count))
            return
        else:
            if(x<a[mid]):
                last_pos = mid-1
            else:
                first_pos = mid+1
    
    print("The Number is not present")
    
a = []
for i in range(1,50):
    a.append(i)
    
binary_search(a,37)
        