# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:50:55 2019

@author: Apratim
"""

#t = int(input("Enter the number:"))
#fact = 1
#for i in range(1,t+1):
 #   if(t==0):
  #      break
   # else:
    #    fact=fact*i
#print(fact)


#for i in range(n):
       # l = []
        #for j in range(n):
        #    l.apppend(0)
            #print(magicSquare[i][j], end=" ")
        #print()
        
#iterative version    
def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product
        
n=int(input('Enter the +ve number:'))
if n<0:
    print('Factorial is not defined on -ve numbers')
else:
    f=factorial(n)
    print('Factorial of ',n, ' is ',f)
        