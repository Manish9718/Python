# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:17:32 2020

@author: HP
"""

==================================

Error Handling
==================================

We use try and except to avoid errors.
Finally: It will always work either except is used or not.
    it give us problem bcz it always work and we want it should run when condition is true.

2 + 's'

try:
    2 + 's'
except:
    print("There is problem and slove it")
finally:
    print("Finally prog run")
    
=====================================
Use of : sys.exc_info()[1]

It basically show us the what error is
=====================================



import sys (system)

try:
    2 + 's'
except:
    print("There is problem and slove it", sys.exc_info()[1])
finally:
    print("Finally prog run")
    
  
    
=====================================
Here we have a problem that it shows error after one exicution.s

def ask():
    try:
        val=int(input("Please enter an integer: "))
    except:
        print("Looks like you have not entered an integer")
    finally:
        print("Finally, exicuted!")
    print(val)
ask()

=====================================
Here it shows error after 2 exicution


def ask():
    try:
        val=int(input("Please enter the value: "))
    except:
        print("You have not enterd the integer")
        val=int(input("Please enter the number"))
    finally:
        print("Finally enterd corectly")
    print(val)
ask()

=====================================


Here we have a problem that every time when value is not even integer: finally is exicuted.

def askint():

while True:
    
    try:
        val = int(input('Please enter an integer : '))
    
    except:
        print('Looks like you did not enter an integer !')
        continue
    else:
        print('Correct !! this is an integer !')
    break
    finally:
        print('Finally block executed !')
    print(val)

=====================================
Finally work when the value is correct.

import sys
def ask():
    while True:
    a=0
        try:
            val=int(input("Please enter the integer: "))
        except:
            print("You have not entered an integer!",sys.exc_info()[1])
            continue
        else:
            print("Yes thats an integer")
            a=1:
            break
        finally:
            if a==1:
                print("Finally exicuted!")
            else:
                print("Try again")
        print(val)

ask()s

=====================================
with files:

import csv,sys
filename='C:/Users/HP/Downloads/Salary_Data.csv'
with open(filename,newline='') as f:
    reader=csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}:{}'.format(filename, reader.line_num, e))
    
    
import sys    
with open("location",'r') as file:
    data=file.reader()
    try:
        for x in data:
            print(x)
    except error as e:
        sys.exit("location {}".format(location))
        
===================================
Question:
    
Handle the exception thrown by the code below by using try and except blocks.
Then use a finally block to print 'All Done.'

x=5
y=0

Ans.

import sys
def div():
    a=0
    while True:
        
        try:
            x = int(input("Please enter the first number: "))
            y = int(input("Please enter the second number: "))
            z = x/y
        except:
            print("Please do not enter 0 as an input, ",sys.exc_info()[1])
            continue
        else:
            print("Eneterd number is correct")
            a=1
            break
        finally:
            if a==1:
                print("All Done")
            else:
                print('Try again')
    print(z)
div()

Q2
Write a function that asks for an integer and prints the square of it.
Use a <code>while</code> loop with a <code>try</code>, <code>except</code>,
<code>else</code> block to account for incorrect inputs.

import sys
def ask():
    a=0
    while True:
        try:
            a=int(input("Please input an integer: "))
            square=a**2
        except:
            print("An error occured! Please try again!, ",sys.exc_info()[1])
            continue
        else:
            a=1
            print("Correctly entered")
            break
        finally:
            if a==1:
                print("Thanks you, your number squared is: ",square)
            else:
                print('Try again!')
ask()