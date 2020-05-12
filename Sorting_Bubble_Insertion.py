# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:12:00 2020

@author: HP
"""
Sorting Allgo.

We have 5 type of Sorting Allgo.
1) Merge Sort : It take a random data to sort and take lot of time.
2) Bubble Sort
3) Insertion Sort
4) Selection Sort
5) Shell Sort

Two sort are most import: Below are the code for the same.

def bubble(a):#name of list = a
    b = len(a) -1 #we have done this because we will use Indexing
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y],a[y+1] = a[y+1], a[y]
    return a
a = [3,6,9,4,5,1]
print(bubble(a))



def insertion(a):
    for x in range(1,len(a)):
        k = a[x] #1
        j = x - 1 # 1-1=0
        while j>=0 and k <a[j]:
            a[j+1] = a[j]
            j -=1
        a [j+1] = k
    return a
a = [1,4,5,6,7,42,5]
print(insertion(a))

    



















