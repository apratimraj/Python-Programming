# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 00:50:12 2019

@author: Apratim
"""
#pythonforbeginners.com
# r+ mode opens the file read as well as write 
with open("file.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()

#random.randrange(2,10,2)
#random.random()
#random.randint(1,5)
#random.choice([1,2,3,4])
#mylist=[1,2,3,4]
#random.choice(mylist)