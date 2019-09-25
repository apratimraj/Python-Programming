# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 00:36:15 2019

@author: Apratim
"""

def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("Enter the +ve number:"))
if n<0:
    print('Undefined for -ve numbers.')
else:
    print('Fibonacci number at position',n, ' is ',fibonacci(n))