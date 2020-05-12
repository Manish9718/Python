# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:01:52 2020

@author: HP
"""
=========================================================================================================================
Generator: with generators we get iterators(iter and next)
=========================================================================================================================
    1) Generators allow us to generate as we go along, instead of holding everything in memory.
    
    2) Generator functions allow us to write a function that can send back a value and
    then later resume to pick up where it left off. 
    
    3)The main difference in syntax will be the use of a yield statement.
    
    4) This type of function is a generator in Python, allowing us to generate a sequence of values over time
    
    7)The main advantage here is that instead of having to compute an entire series of values up front,
    the generator computes one value and then suspends its activity awaiting the next instruction.
    This feature is known as state suspension.
    
    6)Range is a generator. We do not store values in range since we just fetch a single value.

    Ex: range(), map(), filter() 
    
# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3
gencubes(10)
for x in gencubes(10):
    print(x)        

===========================
Yiled
==========================
This Function work same as return and print do however if we want print the values in iteration the we have to use for loop as above.

what is yield?

def fibonica(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for x in fibonica(10):
    print(x)

In the above example we get all the values on after other however some time we need one one value.

Ans we use yield

=========================
Next() and iter(): These are used with yield function to get the next value

Next is used with : Integers
iter is used with : string

def cube(n):
    for num in range(1,n):
        yield num**3
a=cube(10)
a
next(a)
next(a)
next(a)

we have to use yield with next as we need next number from the list or range.s

--------------------------
If we need to work with String

s='heelo'

for l in s:
    print(l)
    
l1=iter(s)

next(l1)
next(l1)
next(l1)
next(l1)

or

def m(n):
    
    for x in n:
        yield x
    
n='hello'
m(n)

c=iter(m(n))
next(c)
next(c)

Q Use a yiled function to get the list datatype?
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

def p(datalist):
    
    for data in datalist:
        yield type(data)
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
type1=iter(p(datalist))

next(type1)