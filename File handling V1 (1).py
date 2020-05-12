# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:44:14 2020

@author: HP
"""

==============================

File Handling

==============================

Q) What do you mean by file handling?
Ans. It is basically handling all structured file with the help of Python language.


Q) What is structured file?
Ans It means the file which you can read and write.

Q) Type of file:
Ans
1. Text file.
2. CSV.        : Comma Seprated value.
3. .xlsx       : It is a file extension for an open XML spreadsheet file format used by Microsoft Excel. 
4. TSV         : Tab seprated value.
5. JSON        : Java script object notation.
                Json = Text
                When exchanging data between a browser and a server, the data can only be text.               
                1.It is a text based data exchange format for structuring data.
                2. It is mainly used to exchange data between server and web application.
                
                Why JSON?
                Ans since it is a text, so easy to read and write.
                
6. .XML       : Extensible markup language.
                
@What is markup language?
Ans using a markup: <name> Manish </name>. So these are markups.

What is .XML?
Ans It is a markup language that is designed to transfer and store data in a specific format that can be processed
by human and machine intelligence.

===========================================================================================

Now how we handle file with python.

*We have 2 type of file:
    1) Text   : Collection of Char.
    2) Binary : Other than Text everything is Binary.



Process of file Handling:
    
     Create  <-----
       |           |
     Open file     |
       |           |
     Work          |
       |           |
     Close file ---

Always remember:
    
    DATA = File
    
    Below are the Modes of file:
    'r' = read (This is a default mode)
    'w' = write
    'a' = append
    'x' = create
    'r+'= reading and writing
    'w+'= write and read
    
    We use 'b' for binary mode.
    
@ When we import data from server we always work on Dummy data.

so how we use it:
    Ex: f=open("location",'rb'/'wb')
        print(f.read())


----------------------------------------- 

1) Open     Syntex = open(file namen mode)
    
            : Always have to use open to a file.
            Ex: open('location of file','r'/'w'/'a')
            before using open providen a variable:
            Ex: F = open('location of file','r'/'w'/'a')

2) read     : It will print the whole file.
              it help in reading the data.
              EX: print(f.read())
              
              if we use print(f.read(5)) : Than it will, print only 1st 5 characters in the file

3) readline : it will help in printing a 1st line.
            EX: print(f.readline())
            
            Use of readline with numbers.
            EX: print(f.readline(1))
            it will give first 1 characters.
            
4) readlines: it will print all the lines one by one in a readable form.
    
5) close: This will close the file.
        Ex: f=open("location",'r')
                print(f.read())
            f.close()
            
6) Seek: This is used to restart the page or text.
        variable.seek(0)
        
for ex if we are reading a page and we are on the last line and then again we need to read from starting.

So in that case "Seek(0)" help in restarting from 1st position.            
----------------------------------------
            
Q) How to open and read a file?
    (Local server or online server)
            
            
file1 = open(location,'r')
print(file1.read())
    
Q) How to write or create a new file?
    
Ans:
Path of ABC: C:\Users\HP\Anaconda3\Lib\site-packages\openpyxl\compat\__pycache__
    
f1 = open('abc','w')
"""Here abc is not a file in computer, So it will first create a new abc file and than write the below content"""

f1.write('Hello new file')
"""If we want to add some more data than we can use this again"""
f1.write("New data in file")

"""Now the problem arise with the above formula that after some time we we need to add more data than we use this
formula again and at that time the previous data got deleted"""
"""Than Append comes to the picture"""
f1.close


Q) How to append a a data in a file?
Ans

f1= open('abc','a')
f1.write("More new data")
f1.close


Q) How to copy a data from a file and than paste it to other file?
Ans We can do it with the help of For Loop:
    
for Ex: we have data in MYdata file and we need to paste it to abc?

f=open('Mydata','r')

f1=open('abc','w')  

for x in f:
    f1.write(x)
    f1.close()
    f.close()
    
    
Q) How to handle pictures and copy paste?
Ans to understand this we have to understand that:
    1) files have characters or values
    2) Images has a binary format
    
So question arises how to deal with this data

For ex : If we have a pic1 file and than we have to create a new file and paste this in a new file pic2.

rb: It means read in binary format.
wb: It means write in binary format.

P=open('pic1','rb')

P1=open('pic2','wb')

for x in P:
    P1.write(x)
    
P1.close()

--------------------------
=====================================================================================

2ndFile Handling Method

=====================================================================================


Q) How to use as file :
    

with open("C:/Users/HP/Downloads/AutoInsurence.txt") as file:   
    data = file.read()


with open("C:/Users/HP/Downloads/AutoInsurence.txt", "r") as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split() 
        """ .split will split all the words in comas"""
        print (word) 


------------------------------

Q) How to delete a file and folder?
Ans
We can do it with the help of os.remove() function

Ex: import os
    os.remove("filename.txt")
    
or we can do this practice:
    if os.path.exists("filename.txt"):
        os.remove("filename.txt)
    else:
        print(this file does not exist)
        
Q) How to delete a folder?
Ans import OS
    os.rmdir("my folder")
    
----------------------------

Q) How to deal with CSV files.
    
    
@Always use import csv

__________________
Read
__________________

Do remember: *use of newline='' in open
             @csv.reader : it will help in reading the file.
             *csv.reader(csvfile: "used as csvfile",delimiter:" ",quotechar="|"): what you want to read
    
    
import csv

with open('C:/Users/HP/Downloads/Salary_Data.csv',newline='') as csvfile:
    spamreader=csv.reader(csvfile,delimiter=' ',quotechar="|")
    for row in spamreader:
        print(", ".join(row))
   

or in simple way we can do


import csv
with open('C:/Users/HP/Downloads/Salary_Data.csv',newline='') as f:
    Reader = csv.reader(f)
    for row in Reader:
        print(', '.join(row))

__________________
Write   
__________________

Do remember: *use 'w' as 'r' is default and we have to use 'w'.
             *csv.writer()
             *.writerow("write what ever you want to write")

with open('C:/Users/HP/Downloads/Salary_Data.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow("something")
    
#import pandas as pd
#df = pd.read_csv("file:///C:/Users/pvine/Desktop/Gurgaon Cognizant/amazon.csv", encoding = 'latin-1')
    
__________________

import csv
with open('C:/Users/pvine/Desktop/New folder/4 Jan/Salary_Data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

__________________

Q) How to avoid the errors if you are sure that your code is correct.
    
Ans. ************************************************************************
        try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    *************************************************************************
        
import csv,sys
filename='C:/Users/HP/Downloads/Salary_Data.csv'
with open(filename,newline='') as f:
    reader=csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}:{}'.format(filename, reader.line_num, e))
        
        
_____________________________________________________________________________________
======================================================================================
Package import from outside to use (Like csv, Audio)
======================================================================================
Packages has multiple modules

module is a file

So collection of Modules is called Packages.

******************
We can create our own Module like in Notepad we can write a code and then save it in .py format and upload
it in the same location where we are run the code.

import life 
life.hello()

-----------------
pwd #used to get the current file directry
-----------------

-----------------
ls #this shows how many file in this directry
-----------------

-----------------
#This is used to change the location of the directry
import os

os.chdir("")
_________________




@pip install csv23
    
@Package import from outside to use (Like to read csv, Audio file)
We have different CSV readers like: CVS or CSV23 as we imported below (They are defined by different users. just a difference)

@How to Google search:
    
    python package for Audio file
    
    or go to github and select the python : Link https://github.com/vinta/awesome-python

@For example we need to read a PDF then we search on the google then we can import just once in a conputer then use it.
    
    
>>> import csv23

>>> with csv23.open_csv('C:/Users/HP/Downloads/lsd_math_score_data.csv') as reader:  # doctest: +SKIP
...     for row in reader:
...         print(', '.join(row))
"""Spam!, Spam!, Spam!'
Spam!, Lovely Spam!, Lovely Spam!'"""


