# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 01:17:17 2019

@author: Apratim
"""

import turtle
from random import randint
turtle.bgcolor("black") # background colour
seurat = turtle.Turtle()

dot_distance = 25
wigth = 5
height =7

seurat.penup()
list_color = ["White","yellow","brown","red","blue","green","orange","pink","violet","green","orange","pink","violet","grey","cyan"]
#python3 program to print
#given matrix in spiral form
seurat.setpos(-250,250)
def spiral(m, n):
    k=0
    l=0
    f = 0
    
    '''
    k= index of starting row
    l= index of starting column
    m= ending row index
    n= ending column index
    i-iterator
    '''
    
    col = randint(0,10)
    seurat.color(list_color[col])
    while(k<m and l<n):
        
        if(f==1):
            seurat.right(90)
            
        # printing the first row from the remaining rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i], end=" ")
        
        k+=1
        f=1
        
        seurat.right(90)
        col = randint(0,10)
        seurat.color(list_color[col])
        # printing the last column from the remaining column
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1], end=" ")
            
        n-=1
        seurat.right(90)
        col = randint(0,10)
        seurat.color(list_color[col])
        if(k<m):
            # printing the last row from remaining rows
            for i in range(n-1, l-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i], end=" ")
            
            m-=1
        seurat.right(90)
        col = randint(0,10)
        seurat.color(list_color[col])
        if(l<n):
            # printing the first column from the remaining columns
            for i in range(m-1, k-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l], end=" ")
            l+=1
            

spiral(20,20)
turtle.done()