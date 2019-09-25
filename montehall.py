# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 01:18:08 2019

@author: Apratim
"""
import random
doors=[0]*3 #for doors
goatdoor=[0]*2 #for goat doors
swap=0 #No of swap wins
dont_swap=0 #no of don't swap wins
j=0
while(j<10): 
    x=random.randint(0,2) #xth door will comprise of BMW
    doors[x]="BMW"
    for i in range(0,3):
        if (i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=int(input("Enter your choice "))
    door_open=random.choice(goatdoor) #open a door that comprises of goat
    while(door_open==choice): #door open shouldn't be equal to choice made by participant
        door_open=random.choice(goatdoor)
    ch = input("Do you want to swap? y/n ")
    if(ch=='y'):
        if(doors[choice]=='Goat'):
            print("player win")
            swap=swap+1
        else:
            print("player lost")
    else:
        if(doors[choice]=='Goat'):
            print("player lost")
        else:
            print("player wins")
            dont_swap=dont_swap+1
    j=j+1

print(swap)
print(dont_swap)