# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:03:41 2020

@author: yamanish
"""

#Print of multiple line.
===========================================================================================
Use of Print in the codes.

We use to get the total output:

n = int(input("enter the value: "))
for i in range(n):
    a=i**2
print(a)  #here print will give total output

and here print is used to get output one by one

for i in range(1,5):
    i=i**2
    print(i)
==========================================================================================

multipleline="""Manish is going where?
with"""

print(multipleline)
-----------------------
'How to add string(words) prior to result of sum,minus,divide and multiply function.'
'Example we need to add- "Total of a+b is" and result'

a=1
b=2
c=a+b
print("Total of a+b is", c) 
print ("total of b-a is", b-a)
print("total of 1*2 is",  a*b)
print("Total of 2/1 is", b/a)

=======================================================
None
=======================================================

x=None (If in future i will assign to it)

future

x=[1,2,3,4,5,6,7]


===============================================
List
===============================================

'list is collection of different values
'list is seprated by comma and use slicing
'list is Mutable
'we use Indexing
'List we use : []

list1=[1,2,3,4,5,6,7,8,9,10]

print(list1)

print(list1*2)

'Assign a new value

list1=[1,2,3,4,5,6,7,8,9,10]
list1[4]='Manish'
print(list1)

--------------------------------------------------------------------------
**imp
'How to add a new number in the list without using a function

list1=[1,2,3,34.0,'string',97,7555,4855.0000,64,'kapil']

list1=list1+['new value']
print(list1)

***Always Remember that we cannot add a new number in the list with INDEXING
***We can only change the value of the existing number with INDEXING
Please check the below Example:

'How to change the value of the below number from the given list:
    
list1=[1,2,3,34.0,'string',97,7555,4855.0000,64,'kapil']

list1[7]='Manish'
print(list1)


---------------------------------------------------------------------
Nested List
---------------------------------------------------------------------

l_1=[66,55,778]
l_2=[44,45,12]
l_3=[11,22,67]


matrix=[l_1,l_2,l_3]
print(matrix)

#way: Nested loop
print(matrix[0][1],matrix[1][1])

#3way: List comprehension
#It is like For loop
first_col=[row for row in matrix]

#It will take first postion from all the matrix
#we can write anything instead of row

first_col=[row[1] for row in matrix]

=========================================================================================
Slicing : To get the number from the series we use :Rule [Start : Stop : Step]
***Always Remember that we cannot add a new number in the list with INDEXING = Use: list=list+[number or string]
***We can only change the value of the existing number with INDEXING
=========================================================================================

'how to find no. from the given list'
'Example- we need first 5 no'

list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[1:6])
-----------------------------
'how to find no. from the given list'
'Example- we need first 5 no'

list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[-5:])

'from below list extract the number:
'2,34.0,97,4855,kapil
    
list1=[1,2,3,34.0,'string',97,7555,4855.0000,64,'kapil']
print(list1[1:24:2])

'from the below data we need:
Kapil then 64

list1=[1,2,3,34.0,'string',97,7555,4855.0000,64,'kapil']
print(list1[-1:-4:-1])

--------------------------------------------------------------------------

    l_1=[1,33,444,555,666,77,799,0,90,98]

print(l_1[-2:-12:-3])

-----------------------------------------------------------------------------
=============================================================================
.Format Method
=============================================================================

'This is a Method through which we can give input:
    
Way 1:
    
print('My name is {}'.format('Manish'))

Way 2:
    
print('We are three firends {0}{1}{2}'.format(': Manish, ','Lekhraj. ','Hunny'))

Way 3: Assigning Keys

print('We are three friens First:{a}, Second:{b}, Third:{c}'.format(a='Manish',b='Lekhraj',c='Hunny'))



===========================================================================
Use of %s and %r
===========================================================================
***here we are using this : .'% (. then ' then %)

Way 1:String 
    
print('I am going to inject %s here.'%'something')

Way2:No

print('Virat kholi scored %s runs.'%90)

Way 3: 2 Variable

print('I am going to inject %s text here, and %s text here.'%('one','two'))

-------------
%r
-------------
If we want to get the string same as written then use: %r

print('Virat kholi scored %r runs.'%'90')

So what ever is after %: all will be shown in that.

=========================================================================
What is Padding?
Ans creating the space is called Padding

Float pointing numbers:
    
print('Float pointing numbers: %5.5F'%(13.14457))

5 = Padding
.5F = How much number after point(.)

If we change the 5F to 2F then :
    
print("Floating points: %8.2F"%(13.14457))
Ans     13.14

=========================================================================

'How to use eval in print'
'Evaluate-eval'

ch=eval(input("Enter a character"))
print(ch)
------------------------
#Input with Int and String

ch=input("Enter a character")
print(ch)

or

hd=int(input("Enter the value: "))
print(hd)

-------------------------
==================================
Dictinory
==================================
#Use dictnory and fetch the address from it.

dict={"name":"Manish",
      "age": 25,
      "Address": "XYZ"}

print(dict["Address"])

#Can we use Numbers as a KEY?

my_dict={1:'student_1',2:'student_2',3:'student_3'}

print(my_dict[3])


----------------------------
#Result should be My name is "Age" should be from using Dict.

MM={"name":"Manish",
      "age": 25,
      "Address": "XYZ"}

print("My age is",MM["age"])
-------------------------------
#How to update a dictionary.
#update

m={0:10,1:20}

m.update({2:30})
print(m)

-----------------------------------------
Nested Dict
----------------------------------------
1.
my_dict={'key1':{'nestkey':{'nestedkey':'Dict inside a dict and dict'}}}

print(my_dict['key1']['nestkey']['nestedkey'])
--------
2.
dict_1={'key_1':{'nest_key':{'nested_key':{'inside_key':[7,9,98,76]}}}}

#for 76 and 9
print(dict_1['key_1']['nest_key']['nested_key']['inside_key'][-1:-6:-2])
--------
'How to know a function do: Press: Tab and then select a fuction and then: Shift + Tab (It only work in Jupyter)
-------
3.
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
print(d['k1'][0]['nest_key'][1][0])
--------
4.
'How to get "hello"
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2])

'No, we cannot sort a dictinory since sorting require ordered data type, which is a list.

_______________________________________________________________________
For loop in Dict: Use of variable.items() and sorted(variable.value())
_______________________________________________________________________

1.
d={'k1':1,'k2':2,'k3':3}

for i in d:
    print(i)
       
'If we use only d in for loop then it will only fetch the Keys not the values

2.
'How to fetch Keys and values together?
'Ans we can with the help of d.items (Variable.items)

d={'k1':1,'k2':2,'k3':3}
for i in d.items():
    print(i)
    
or to get this type of Answer: k1:1,k2:2,k3:3,

d={'k1':1,'k2':2,'k3':3}
for i,j in d.items():
    print(i,end=":")
    print(j,end=",")

3.
'How to get the values in Ascending order?
'Ans we can use sorted(d.value())

d={'k1':3,'k2':2,'k3':1}
sorted(d.values())

=========================================
Tuple
=========================================

t_1=(1,2,33,44,5,5)
type(t_1)

#collection of different value
t2=('sam','ram',5.878,87)
t2


t1=(1)
t1=(1,)
t1
type(t1)

'Q1. Can we assign a single value to a Tuple
'Ans Yes we can but we have to use ,(comma after that)

'Q2. can we make tuple without ()
'Ans yes we can which is called tuple packing

t1=1,2,4
t1
type(t1)

#2 Method : Index and Count.

=========================================
-----------------------------------------------------------------------------------------------------------
#Count

g=[1,2,3,3,4,3,5,6,6,6]

g.count(3)
---------------------------
Conditional Statement: If, elif
--------------------------
#Conditional Statement
# If , Elif and Else
#Logical operator : and , or and not

#If

a = 33
b = 33

if a>b and b==a:
    print("ABC")
else:
    print("BCA")

#Elif
#Use a formula when no condition is True by using if, elif, else.

a=33
b=33

if a>b:
    print("A")
elif b>a:
    print("B")
elif b!=a:
    print("C")
else:
    print("No")

#Short Hand

a=330
b=330

print("A") if a>b else print("C")

#Number is even or odd
#Use if condition to get a Even and ODD value.

K=int(input("Enter a number: "))

if K%2==0:
    print("Yes")
else:
    print("No")

#Nestedif

x=41

if x>10:
    print("Yes")
    if x<10:
        print("No")
    else:
        print("Not considered")

#Use of Not
x="Hello python"

print("Hello" not in x)

----------------
Q) use a condition where result should be even or add as per b.
    Also a is greater than 10 or not.
'if & else statement'

a=4
b=a%2
if b==0:
    print("Even")
    if a>5:
        print("More than 5")
    else:
        print("Less than 5")
else:
    print("Odd")
print("Bye")
-----------------
'if , elif & else'

a=2
if a==0:
    print("Equals to 0")
elif a==1:
    print("=1")
elif a==2:
    print("equal 2")
else:
    print("Not=")

===============
Polindrome
===============
#Use of Polindrome with String

x=input("Enter a String: ")
if (x==x[::-1]):
    print("yes")
else:
    print("No")

#Use of Polindrome with Number
#we have to make a code like we use to do when we play a game, think a number and the divide it like that

num=int(input("Enter a number: "))
item=num
rev=0
while num>0:
    dig = num%10  #if input is 44 than 44%10=0
    rev = rev*10 + dig #r=0 and 0*10=0, 0+0=0 
    num = num//10  #44/10=0
    #So final result is 0 than it means if number result is 0 so yes and if not than no.
if (item==rev):
    print("Awesome")
else:
    print("Not fullfiled")



-------------
LOOP: 
Do remember that how to use print:
1) If print is used like below means you just want a result.
    if x in y:
    
print :
Ans 245
    
2) If x in y:
    print()
It means that we want a list of result not a single one.
Ans: 2
     3
     4
 
---------------

# LOOPS
#We have 3 types of Loop
#FOR, WHILE, DO WHILE.

a=["a","b","c"]

for i in a:
    print(i)

#Use of for with range
#Q provide 0 to 9 value

for i in range(0,10,1):
    print(i)

#For loop with if condition
#use a formula to get the value from 0 to 20 not divided with 5.

for i in range(0,21,1):
    if i%5!=0:
        print(i)

#Nested loop
#Result should be:
"""0  , 10
0  , 11
0  , 12
0  , 13
1  , 10
1  , 11
1  , 12
1  , 13
2  , 10
2  , 11
2  , 12
2  , 13"""

for num1 in range(3):
    for num2 in range(10,14):
        print(num1," ,",num2)

'''So do remember to use nested loop when you want to add more data at same line.'''
'''if is a condition'''
---------------------
'break it will go till mango and then break '

fruits=["apple","mango","banana"]
for x in fruits:
    if x == "banana":
        break
    print(x)
--------------------
#Multily var* var in list numbers=[2,4,6,8]

numbers=[2,4,6,8]

for var in numbers:
    sq=var*var
    print(sq)
-------------------
#Print "item in list1 is" with fruit name
#list1=['apple','banana','grapes','mango']

list1=['apple','banana','grapes','mango']
for a in list1:
    print("item in list1 is",a)

--------------------
#Result to be 
#item  1  is  Apple
#item  2  is  Mango
#item  3  is  Banana
#item  4  is  Grapes


fruits = ["Apple","Mango","Banana","Grapes"]
i=1
for x in fruits:
    print("item",i, "is", x)
    i=i+1

#Extract the value from the list upto 237 and it should be even number.

numbers = [2,2,2,3,4,45,556,6,6,7,7,7,7,65,4,33,237,4565,68767,97689,78]

for x in numbers:
    if x==237:
        break
            
    if x%2!=0:
        continue
      
    print(x)
    
#So here we have used break statement first since when the code run it will first check the 237 then take the vale.
-------------------------------------------------------------------
#Use a formula to get the square of the value we input.

n = int(input("enter the value: "))
for i in range(n):
    a=i**2
print(a)

So remember to use print in the same position so that we will get the value square.

-----------------------------------
==============================
Break, Countinue and pass
==============================
break: Breaks out of the current closest enclosing loop.
continue: Goes to the top of the closest enclosing loop.
pass: Does nothing at all.

Pass is used when we are not sure about the function and the function will not show an error.

lst = list(range(10))
for i in lst:
    if i==8:
        pass

Break will stop the loop when the condition is satisfied.

lst = list(range(10))
for i in lst:
    if i==8:
        break
    else:
        print(i)

Continue

This will skip the 3 from the list
lst = list(range(10))
for i in lst:
    if i==3:
        continue
    else:
        print(i)
        

============================================================================
Enumerate: This operator is used to get the Index and value at the same time.
============================================================================

Manually
a=0
for i in range(1,7):
    print("Index {} value {}".format(a,i))
    a+=1
    
with enumerate: Here: ('abcde') we can only give Tuple not List or other.

String    
for i,letter in enumerate('abcde'):
    print("index: {}, value: {}".format(i,letter))

Numbers
for x,y in enumerate(range(1,20)):
    print("Index: {}, Value: {}".format(x,y))


====================================================================
ZIP: when we have more then 1 list (ZIP means collecting all data in one)
Element in both the list should be same
====================================================================

l1=[1,2,3,4]
l2=['a','b','c','d']

list(zip(l1,l2))

if element in both the string are different then it will result min combination num.
Here list is different

l1=[1,2,3,4,5,6,7,8,9,10]
l2=['a','b','c','d']

list(zip(l1,l2))
    
ans is till the 4th position: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

================================================================= 
In Operator: Will give us True or False Result
=================================================================

list1=[1,2,3,4,5]

3 in list1

==================================================================
Min and Max
==================================================================

list1=[1,2,3,4,5]

min(list1)

max(list1)

==================================================================
Shuffle 
==================================================================


list1=[1,2,3,4,'v']
from random import shuffle

shuffle(list1)
print(list1)

==================================================================
Randomint
from random import randint
==================================================================

randint(0,100)

==================================================================
reduce :this is imported from functools
==================================================================

reduce function

This basically work with lambda function

Here reduce is taking "a" and perform an activity with adjusent value. Then with result it perform an activity
with the adjusent.

So 2+2=4, 4+4=8 

for Ex:
from functools import reduce
l=[2,2,4]

reduce(lambda a,b:a+b,l)

==================================================================
map
==================================================================

Map basically help in combining different list together and retun with a function. Also can be used in different ways as it take
a function and list.

For ex: we have different 3 list and we need to apply a function to all lists.
Then we can just use : map("Function name",Listname)

l1=[1,2,3]
l2=[1,2,3]
l3=[1,2,3]
l4=[l1,l2,l3] 

==================================================================
complex
==================================================================
we can create an imaginary number:
    Complex number = 2+3i (Here 3 is a real no and i is a imaganery no)
    i = iota (3**2)*(1/2)
    
a=complex(a+2j)
a   

==================================================================
All and Any Function
==================================================================

All any function

All: if all condition is True then True

a=[True,True,True]
all(a)

a=[True,False,False]
any(a)
    
Any : if any of in the list is True then return True.

==================================================================
__________________________________________________________________

MODULES
__________________________________________________________________
==================================================================

==================================================================
collections Module Counter: Always use Capital C in Counter
==================================================================
Counter : It help in founding how many time an item is used.

Counter is a Dict sub class

from collections import Counter
l=[1,1,1,1,1,2,2,2,2,3,3,3,3,4]
Counter(l)

Ans Counter({1: 5, 2: 4, 3: 4, 4: 1})
******

we can also use it with words

s = 'How many times does each word show up in this sentence word times each each word'

word=s.split()

c=Counter(word)
******

Now there are some methods of Counter

s = 'How many times does each word show up in this sentence word times each each word'

word=s.split()

c=Counter(word)

c.most_common(2) #this gives us the most common words used.
***********************************************************************
Common patterns when using the Counter() object
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
***********************************************************************
==================================================================
Datetime Module
==================================================================

datetime: 
    
Python has the datetime module to help deal with timestamps in your code. Time values are represented with the time class.
Times have attributes for hour, minute, second, and microsecond. They can also include time zone information.
The arguments to initialize a time instance are optional, but the default of 0 is unlikely to be what you want.


1) time
    
datetime.time(hour,minute,second,microsecond)

EX:
import datetime
t=datetime.time(4,20,3,9)
print(t)  # Ans. 04:20:03.000009
# Let's show the different components
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

We can also check the min and max values a time of day can have in the module:

print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution) #this give us the up to what it can hold a time.

Ans
Earliest  : 00:00:00
Latest    : 23:59:59.999999
Resolution: 0:00:00.000001
-----------------------------------

2. Dates
datetime (as you might suspect) also allows us to work with date timestamps.
Calendar date values are represented with the date class.
Instances have attributes for year, month, and day. It is easy to create a date representing today’s
date using the today() class method.

today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)

Ans

2018-02-05
ctime: Mon Feb  5 00:00:00 2018
tuple: time.struct_time(tm_year=2018, tm_mon=2, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=36, tm_isdst=-1)
ordinal: 736730
Year : 2018
Month: 2
Day  : 5
-------------
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)

Ans

Earliest  : 0001-01-01
Latest    : 9999-12-31
Resolution: 1 day, 0:00:00


Q. Another way to create new date instances uses the replace() method of an existing date.
   For example, you can change the year, leaving the day and month alone.

d1=datetime.date(2019,4,29)
print(d1)

d2=d1.replace(year=2020)
print(d2)

=================================================================
timeit: this is used to check the run time of our code.
=================================================================
How much time our code take run

Timing your code
Sometimes it's important to know how long your code is taking to run, or at least know if a particular line of code is slowing down your entire project. Python has a built-in timing module to do this.

This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one. It avoids a number of common traps for measuring execution times.

Let's learn about timeit!

Here we are comparing the time taken by a code: loop, list comprehension & map. 

# For loop
import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

#list comprehension
import timeit
timeit.timeit('"-".join([str(n) for n in range(100)])',number=10000)

#Map()
import timeit
timeit.timeit('"-".join(map(str,range(100)))',number=10000)

we can also do it with magic function %timeit

import timeit
%timeit "-".join(str(n) for n in range(100))

%timeit "-".join([str(n) for n in range(100)])

%timeit "-".join(map(str, range(100)))

=================================================================
Debuging
=================================================================

We can debug our code when the code is showing some error:
    
For ex:
    
import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)

we quit by using 'q' from the pdb
---------------
============================================================================================
Regular Expressions
============================================================================================
Regular expressions are text-matching patterns described with a formal syntax.

Do remember
using search will give the result but not print
using findall will print the result
using match will give the result only

1.
Searching for Patterns in Text
One of the most common uses for the re module is for finding patterns in text

import re

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

#This is used to get single term1 from the patterns.
for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' %(pattern,text))
    
    #Check for match
    if re.search(pattern,text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')

------------------------------------
2. ****Interview questions?
Split with regular expressions
Lets see how we can split with the re syntax. This should look similar to how you used the split() method with strings.

Ans.
import re
# Term to split on
split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

re.split('@',phrase) #or we can also use re.split(split_term,phrase)

-----------------------------------
3.
Finding all: means finding the duplicates and how many time that is repeated.

You can use re.findall() to find all the instances of a pattern in a string. For example:

# Returns a list of all matches
re.findall('match','this is a match list in which is a match')
#Return is
re.findall('is','this is a match list in which is a match')
Ans. ['is', 'is', 'is', 'is'] #here it is showing is 4 times bcz this has 'is', list has is and more.

----------------------------------
4.Repetition Syntax

Repetition Syntax
There are five ways to express repetition in a pattern:

A pattern followed by the meta-character * is repeated zero or more times.
Replace the * with + and the pattern must appear at least once.
Using ? means the pattern appears zero or one time.
For a specific number of occurrences, use {m} after the pattern, where m is replaced with the number of times the pattern should repeat.
Use {m,n} where m is the minimum number of repetitions and n is the maximum. Leaving out n {m,} means the value appears at least m times, with no maximum.
Now we will see an example of each of these using our multi_re_find function:
    
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                's*d$',         # s followed by n numbers but end with d
                ]


-----------------------------------
5.
Exclusion
We can use ^ to exclude terms by incorporating it into the bracket syntax notation.
For example: [^...] will match any single character not in the brackets. Let's see some examples:

Use [^!.? ] to check for matches that are not a !,.,?, or space. Add a + to
check that the match appears at least once. This basically translates into finding the words.    

import re
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

re.findall('[^!.? ]+',test_phrase) 

QWrite a Python program where a string will start with a specific number.
Ans
import re
def match_num(string):
    text = re.compile("5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))
---------------------------------
6.
Character Ranges¶

As character sets grow larger, typing every character that should (or should not) match could become very tedious.
A more compact format using character ranges lets you define a character set to include all of the contiguous characters
between a start and stop point. The format used is [start-end].

Common use cases are to search for a specific range of letters in the alphabet.
For instance, [a-f] would return matches with any occurrence of letters between a and f.   


test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters

Ans
['his', 'is', 'an', 'example', 'sentence', 'ets', 'see', 'if', 'we', 'can', 'find', 'some', 'letters']
['T', 'L']
['This', 'is', 'an', 'example', 'sentence', 'Lets', 'see', 'if', 'we', 'can', 'find', 'some', 'letters']
['This', 'Lets']

7.
Escape Codes¶
You can use special escape codes to find specific types of patterns in your data, such as digits, non-digits, whitespace, and more. For example:

Code	Meaning
\d	a digit
\D	a non-digit
\s	whitespace (tab, space, newline, etc.)
\S	non-whitespace
\w	alphanumeric
\W	non-alphanumeric

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

Ans.
Searching the phrase using the re check: '\\d+'
['1233']


Searching the phrase using the re check: '\\D+'
['This is a string with some numbers ', ' and a symbol #hashtag']


Searching the phrase using the re check: '\\s+'
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


Searching the phrase using the re check: '\\S+'
['This', 'is', 'a', 'string', 'with', 'some', 'numbers', '1233', 'and', 'a', 'symbol', '#hashtag']


Searching the phrase using the re check: '\\w+'
['This', 'is', 'a', 'string', 'with', 'some', 'numbers', '1233', 'and', 'a', 'symbol', 'hashtag']


Searching the phrase using the re check: '\\W+'
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #']

-----------------
 8.https://www.youtube.com/watch?v=Q_xYRXA8McA
Match: Used to test the input string with a specific pattern or not.

here we also use: r'' (it means Raw string)

How we use match: basically we check weather the string starts with the given input or not

For ex: **Remember this is case specific.
    
import re
line='Python and Java gives Jython'
re.match(r'Java',line)  #this means that the line starts with Java or not

Ans as the result is wrong then it give us a none result, if we change it to Python.

import re
line='Python and Java gives Jython'
re.match(r'Python',line)

9.
sub()
sub() function in the re module can be used to replace substrings. The syntax for re. sub() is re. sub(pattern,repl,string)

re. sub(pattern,repl,string)

pattern= what is the pattern now
repl= what pattern you want  :  '\\1/\\2/\\3' this shows how we need it like seprated with "/" or space or "-" 
and //1,//2 is the position
string= from where

import datetime
original="2019-06-20"

#re. sub(pattern,repl,string)
#pattern=r'(\d{4})-(\d{1,2})-(/d{1,2})'
a=re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3/\\2/\\1',original)
a



**************************************************
Question related to Regular expression: https://www.w3resource.com/python-exercises/re/#EDITOR
    
Q1.Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
l='As He was a child with Age 25'
Ans.

import re
l='As He was a child with Age 25'
if re.search("[A-Za-z0-9]",l):
    print("Yes")
else:
    print("No")
    
Q2.
2. Write a Python program that matches a string that has an a followed by zero or more b's
l='abb an ab asdfe ahut adddddd aasd ad'
Ans
l='abb an ab asdfe ahut adddddd aasd ad'
import re
re.match('[ab*]',l)

or

import re
def text_check(text):
    pattern='ab*'
    #if we change the * into + then 2 result will be wrong    
    if re.search(pattern,text):
        return 'yes'
    else:
        return 'no'
    
print(text_check('ab'))
print(text_check('ac'))
print(text_check('abbc'))

Q3.Write a Python program to find sequences of lowercase letters joined with a underscore.
print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

Ans
import re
def text_match(text):
    
    pattern='[a-z]+_[a-z]'
    
    if re.search(pattern,text):
        return 'yes'
    else:
        return 'no'

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

Q4
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))

Ans
import re
def text_match(text):
        patterns = 'a*b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))

Q5
Write a Python program that matches a word at the beginning of a string.
print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))

Ans
import re
def text_match(text):
        patterns = 'a'
        if re.match(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))

Q6
Write a Python program that matches a word at the beginning of a string.
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))

Ans
import re
def text_match(text):
        patterns = '^\w'
        if re.match(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog.")) #here we have used space.

Q7
Write a Python program that matches a word at the end of string, with optional punctuation.
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))

Ans
import re
def text_match(text):
        patterns = '\S$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))

Q8
Write Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
"Exercises number 1, 12, 13, and 345 are important"

Ans
import re

r=re.finditer('[0-9]{1,3}',"Exercises number 1, 12, 13, and 345 are important")
for x in r:
    print(x.group(0))
    
Q9.
# 19. Write a Python program to search some literals strings in a string. Go to the editor
Sample_text='The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'

Ans
Sample_text='The quick brown fox jumps over the lazy dog.'
import re

patterns=['fox','dog','hourse']

for x in patterns:

    if re.search(x,Sample_text):
        print("Match")
    else:
        print("Not Matched")
        
Q10
Write a Python program to search a literals string in a string and also find the location within the original string
where the pattern occurs. Go to the editor

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

Ans should be: Found "fox" in "The quick brown fox jumps over the lazy dog." from 16 to 19 

import re
pattern='fox'
Sample_text='The quick brown fox jumps over the lazy dog.'
match=re.search(pattern,Sample_text)
e=match.start()
f=match.end()
print('Found %s in %s from %s to %s'%(match.re.pattern,Sample_text,e,f))

Q11
Write a Python program to replace whitespaces with an underscore and vice versa.
text='Python Exercise'

import re
text='Python Exercise'
text=text.replace(" ","_")
print(text)
text=text.replace("_"," ")
print(text)

Q12
Write a Python program to extract year, month and date from an url.
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

Ans
import re
def extract_date(url):
        return re.findall(r'(\d{4})/(\d{1,2})/(\d{1,2})', url) #here "/" these are used to create date as we do in 2020/2/23
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))

Q13
Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
original="2019-06-20"

Ans
import datetime
original="2019-06-20"

#re. sub(pattern,repl,string)
#pattern=r'(\d{4})-(\d{1,2})-(/d{1,2})'
a=re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1',original)
a

import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

Q14
Write a Python program to find all words starting with 'a' or 'e' in a given string.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

Ans
import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#find all the words starting with 'a' or 'e'
list = re.findall("[ae]\w+", text)
# Print result.
print(list)

Q15
Write a Python program to replace all occurrences of space, comma, or dot with a colon
text = 'Python Exercises, PHP exercises.'

import re
text = 'Python Exercises, PHP exercises.'
a=re.sub('[" ",.]+',":",text)
a

Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.

import re
text = 'Python Exercises, PHP exercises.'
a=re.sub('[" ",.]+',":",text,2)
a

Q16
Write a Python program to find all three, four, five characters long words in a string.

text = 'The quick brown fox jumps over the lazy dog.'

import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{3,5}\b", text))

Q17
Write a python program to convert camel case string to snake case string.
'PythonExercise'

Ans
def camel_to_snake(word):

    import re
    return "_".join(x.lower() for x in word.split())
camel_to_snake('PythonExercise')

Q18
Write a python program to convert snake case string to camel case string.
'python_exercises'

Ans
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('python_exercises'))

Q19
Write a Python program to remove all whitespaces from a string.
text1 = ' Python    Exercises '

Ans
import re
text1 = ' Python    Exercises '
print("Original string:",text1)
print("Without extra spaces:",re.sub(r'\s+','',text1))

Q20
Write a Python program to remove everything except alphanumeric characters from a string.
text1 = '**//Python Exercises// - 12. '

import re 
text1 = '**//Python Exercises// - 12. '
pattern='\w+'
a=re.findall(pattern,text1)
"".join(a)

Q21
Write a Python program to find all adverbs and their positions in a given sentence.
text = "Clearly, he has no excuse for such behavior."

Ans
import re
text = "Clearly, he has no excuse for such behavior."
for m in re.finditer(r"\w+ly", text):
    print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
    
Q22
Write a Python program to insert spaces between words starting with capital letters.
print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))

Ans
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))

=================================
list comprehension: There is no need to declare a variable and print. It autmatically work and print.
==================================
Manually
st = 'hello'
lst=[]

for x in st:
    lst.append(x)
print(lst)

with lis comp:

string
st = 'hello'    
lst=[x for x in st]
lst

Number
num1=[1,2,3,4]
number2=[x for x in num1]
number2

Now the first x is doing the operation
and second x is doing for loop.

num1=[1,2,3,4]
number2=[x*2 for x in num1]
number2

list comp with if condition

num1=[1,2,3,4]
number2=[x for x in num1 if x%2==0]
number2


f1=[]
c=[0,10,20.1,30.2]

for i in c:
    f=((9/5)*i + 32)
    f1.append(f)
print(f1)


Q. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

list1=[x for x in range(1,50) if x%3==0]
list1

Q. Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
f=[x[0] for x in st.split()]
print(f)
===================================================
=========================
#While loop
#Print Manish 5 times
=========================

i=1
while i<=5:
    print("Manish")
    i=i+1

#Can we do nested loop
#Yes
#Q: We need Manish 5 time and in same line we nedd 4 times Rocks
#To print in the same line we have to use a code : end=""
    
i=1
while i<=5:
    print("Manish",end="")
    j=1
    while j<=4:
        print("Rocks",end="")
        j=j+1
    
    i=i+1
    print()
----------------------------------

#Use of while loop with input. How many Candy you need, print those candy.

i=int(input("Enter the no of Candy: "))
while i <=5:
    print("Candy")
    i+=1
#or
    
a=int(input("candy ?"))
i=1
while i<a:
    print("candy")
    i+=1
------------
#'if input is more then the given value' for the previous question

a=int(input("Enter the no of candy: "))
av=10
i=1
while i<=a:
    """Always remember the value of i will start from 1 and then apply the condition"""
    """here the value of i is one so it is less then a and av. it will not break and print candy"""
    """but when i+=1 goes beyound 10 to 11 then again it check the conndition and print "Out of stock"""
    if i>av:
        print("Out of stock")
        break
    print("Candy")
    i+=1
print("Bye")
-------------

'while Loop increasing order/ascending order'

a=1
while a <=5:
    print("Yes")
    a+=1
    
    #or
a=1
while a <=5:
    print("Welcone",a)
    a+=1

'while Loop increasing order/descending order'

a=5
while a >=1:
    print("NO")
    a-=1
    
#or
    
a=5
while a >=1:
    print("No",a)
    a-=1
----------------------

##use while statement with If.

x=1
while(x<5):
       print(x)
       x +=1
else:
    
    print("XYZ")


---------------------------------
#Ask about how many candy you want.
#Stop when need excess candy then available
#Here if i>av: we havwe used i instead of x bczif we use x the directly result will shown and candy will not show.
#so we need to print first all the avilable candy and than when it goes beyond the limit show out of stock.

x = int(input("How many candy you want"))

i = 1
while i <= x:
    print("Candy")
    i+=1
 # Now
 
x = int(input("How many candy you want"))
av=5
i = 1
while i <= x:
    if i>av:
        print("Out of stock")
        break
    
    print("Candy")
    i+=1
   
print("Bye")
----------------------------------------
#Print the number from 1 to 20 but not divisible by 3 or 5

for i in range(1,50):
    if i%3==0 or i%5==0:
        continue
    print(i)

print("Bye")

----------------------------

#For loop practice
#'For loop is used for sequence'

a=[1,2,3,4,5]
for i in a:
    print(i)
    
-------------------
#For loop with name

a="Manish"
for i in a:
    print(i)
-----------------
#For loop with Range

for i in range(10):
    print(i)
---------------
#for loop with range in reverse order, fromm -1.

for i in range(10,5,-1):
    print(i)
--------------
# for loop with if condition: print 1 to 25 and no not divided by 5.

for i in range(1,26):
    if i%5!=0:
        print(i)
        
        or

for i in range(1,26):
    if i%5==0:
        print(i)
-------------
"""FOR LOOP"""
-------------
#Print welcome 5 times and in the same line of single print write Yes 5 times.

a=1
while a <=5:
    print("Welcome",end="")
    j=1
    while j <=5:
        print("Yes",end="")
        j+=1
    a+=1
    print() 
    """So when we use print at the last it will give a series result not in a line"""
---------------
"""Print list=['Manish','Kapil','Hunny','Lekhraj']"""
"""Result should be = 
Manish Welcome To our home 
Kapil Welcome To our home 
Hunny Welcome To our home 
Lekhraj Welcome To our home """

def d(n):
    for x in n:
        print(x," welcome to our home")
    print()
n=['Manish','Kapil','Hunny','Lekhraj']
d(n)

---------------
#Print Welcome 5 times
#Print One 5 times
#Print Two 4 times in the same line.

a=1
while a<=5:
    print("Welcome",end="")
    b=1
    while b<=1:
        print("One",end="")
        c=1
        while c<=4:
            print("Two",end="")
            c+=1
        b+=1
    a+=1
    print()

or with For loop


for x in range(5):
    print("welcome",end="")
    for y in range(1):
        print(" One",end="")
        for z in range(4):
            print(" Two",end="")
    print()
    
--------------------------------
=================================================
.split use

Basically used to get the the word from a string
=================================================

To the take all words from a line we have to use: .split()


st = 'Print only the words that start with s in this sentence'
for x in st.split():
    if x[0]=='s':
        print(x)

=========================================================================================================================
.split use  to get the two words from the same string
        
***This is Important: How we can use" f,s = text.split(" ") " to getb the data from the same string with different words
=========================================================================================================================

Write a function takes a two-word string and returns True if both words begin with same letter
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
    
def animal_crackers(text):
    
    f,s = text.split(" ")
    #basically we are splitting the text in the same line.
    if f[0]==s[0]:
        return True
    else:
        return False
    
text=input("Please enter the string: ")
animal_crackers(text)

-------------------
#Use of stars in the while loop

a=1
while a<=1:
    print("*")
    a+=1
    b=1
    while b<=4:
        print("*",end="")
        b+=1
    print()
    c=1
    while c<=1:
        print("*",end="")
        c+=1
    print()
    d=1
    while d<=4:
        print("*",end="")
        d+=1

print()
---------------------
#Print 1 to 100 counting

for x in range(1,11):
    while x<=100:
        print(x," ",end="")
        x=x+10
    print()
    
or

for x in range(1,11):
    while x<=100:
        print(x,end="\t")
        x+=10
    print()
-------------------
#Print table from 2 to 10
#Here \t means to get the result in proper format with spaces.

for x in range(2,21):
    for k in range(1,11):
        print(x*k,end="\t")
    print()  
    
-----------------
#Print 
#*
#* * 
#* * * 
#* * * * 
#* * * * * 

a=1
while a<=1:
    print("*")
    a+=1
    b=1
    while b<=2:
        print("*",end="")
        b+=1
    print()
    c=1
    while c<=3:
        print("*",end="")
        c+=1
    print()
    d=1
    while d<=4:
        print("*",end="")
        d+=1
    print()
    e=1
    while e<=5:
        print("*",end="")
        e+=1
print()

or

num=int(input("Enter the number: "))
for a in range(1,num+1):
    for b in range(1,a+1):
        print("*",end="")
    print()

#Explain:
'''1.for a in range(1,num+1):''':means total input range= 5 so range(1,(5+1)=6)
'''for b in range(1,a+1):''':means range no is 1 than star range=(1,2)=star=1
'''so on range no is 2 than star range(1,3)=star 2'''
    

or

num=int(input("enter the no. of rows"))
k=1
for  a in range(1,num+1):
    for b in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print() 

----------------
'print 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
#Here we have not used nested for loop bcz we need * in series.

co=int(input("Enter the value: "))
for x in range(1,co+1):
    print(" "*(co-x),"* "*x)

#Explain: " "*(Co-x)
    #" "*(5-1)=4: Space i need is 4, x should be printed.
    #"* "*1=1 (It means number of star needed is
    #when range is 2 than "* "*2=2, so start will be 2 and so on.
---------------
'print
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    *

n=int(input())
for x in range(1,n):
    print(" "*(n-x),"* "*x)
for x in range(5,0,-1):
    print(" "*(n-x),"* "*x)
print()  

#Remember to use this:for x in range(y-1,0,-1):
--------------------------

3.Write a Python program to construct the following pattern, using a nested for loop
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

Ans
n=int(input())
for x in range(1,n):
    for y in range(x):
        print(" *",end="")
    print()
for x in range(5,0,-1):
    for y in range(x):
        print(" *",end="")
    print()

----------------
#Print
* * *
*   *
* * *
*   *
*   *

a=5
if a<=5:
    print("* * *")
    if a<=5:
        print("*   *")
        if a<=5:
            print("* * *")
            if a<=5:
                print("*   *")
                if a<=5:
                    print("*   *")

#Remember to use same count since we need to use TRUE value.
------------------
#Print

  * *
*   
*    * **
*    *  *
  * *   *

a=3
if a<=3:
    print("  * *")
    if a<=3:
        print("*")
        if a<=3:
            print("*    ****")
            if a<=3:
                print("*    *  *")
                if a<=3:
                    print("   * *  *")
    
--------------------
#print:
####
####
####
####

for x in range(4):
    for y in range(4):
        print("#",end="")
    print()  

or

n=int(input())
for x in range(1,n+1):
    print("#",end="")
    for y in range(1,5):
        print("#",end="")
    print()    
-------------------
#Print table of 3,4 and 5.

x=3
while x <=5:
    y=1
    while y<=10:
        print(x,"*",y," =",x*y)
        y+=1
    x+=1
    print()

or

for x in range(2,21):
    for y in range(1,11):
        print(x,"*",y,"=",x*y)
    print()

or

x=2
while x <=4:
    y=1
    while y<=10:
        print(x*y)
        y+=1
    x+=1
    print()
==================================================================
Question related to loop and condition
==================================================================

1. Write a Python program to find those numbers which are divisible by 7 and
 multiple of 5, between 1500 and 2700 (both included).

Ans

def mul(n):
    
    lst=[]
    for x in range(1500,2701):
        if x%5==0 and x%7==0:
            lst.append(x)
    print(lst)
    
mul(n)

2. Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess
is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

Ans
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')

3.Write a Python program to construct the following pattern, using a nested for loop
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

Ans
n=int(input("Enter the number of star: "))
for x in range(1,n):
    for y in range(x):
        print("* ",end="")
    print()
for x in range(n,0,-1):
    for y in range(x):
        print("* ",end="")
    print()
    
4. Write a Python program to count the number of even and odd numbers from a series of numbers.
Ans

def od(n):
    a=0
    b=1
    
    for x in n:
        if x%2==0:
            a+=1
        else:
            b+=1
    print("Even number in the list are: ", a)
    print("Even number in the list are: ", b)    

n=[2,3,2,4,2,865,35,332]
od(n)

print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd) 

5. Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]   

def item1(n):
    
    for x in n:
        print(x,": ",type(x))
    
n=[1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
item1(n)

or

def item1(n):
    lst=[]
    for x in n:
        a = (x,": ",type(x))
        lst.append(a)
    print(lst)
n=[1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
item1(n)
    
6.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5

Ans.
for x in range(6):
    if x%3!=0:
        """BCZ of x%3!=0 we are not getting 0"""
        """If we will use x==3 and than continue we will get 0"""
        print(x,end=" ")
print()

or

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")

or in function

def item1(n):
    lst=[]
    for x in n:
        a = (x,": ",type(x))
        lst.append(a)
    print(lst)
n=[1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
item1(n)

7. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34

Ans
***Remember here loop is just used to do the thing as number of time inputed by the user.
***Thats why we have returned or yield a

def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
for num in genfibon(10):
    print(num)
        
or in function

def fib(n):
    a=1
    b=0
    if n==1:
        return a
    else:
        for x in range(1,n+1):
            c=a+b
            a=b
            b=c
            print(c)
    
n=int(input("Please enter the no for Fibonacci series: "))
fib(n)
        
8. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of
the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and
five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz

Ans

for x in range(50):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
        continue
    elif x%3==0:
        print("Fizz")
        continue
    elif x%5==0:
        print("Buzz")
        continue
    print(x)
    
or in Function

def outp(n):
    
    for x in range(1,n+1):
        if x%3==0 and x%5==0:
            print("FizzBizz")
        elif x%3==0:
            print("Fizz")
        elif x%5==0:
            print("Bizz")
        else:
            print(x)
    
n=int(input("Please enter the range: "))
outp(n)
    
9.Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and
print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010

Ans
items = []
num = [x for x in input("Enter the binary no please: ").split(',')]
"""This statement split the binary no. seprately"""
for p in num:
    """This statement will ittrate the first binary number, which is 0100"""
    x = int(p,2)
    """This line is converting the binary number into interger"""
    """Int takes 2 arguments: Item and base"""
    """ 3 = 0100, 4 = 0011"""
    if x%5==0:
        """If (0100:3)=> 3%5==0"""
        item.append(p)
print(",".join(item))


10 Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2

a=0
b=0
n = input("Input a string")
for x in n:
    if x.isdigit():
        a+=1
    elif x.isalpha():
        b+=1
    else:
        pass
print(a)
print(b)

11 Write a Python program to check the validity of password input by users. Go to the editor
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

Ans

import re
p= input("Input your password")
x = True #This s a boolean statement
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False # if above x is false then break
        break

if x:
    print("Not a Valid Password")
    
12.Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is 
an even number. The numbers obtained should be printed in a comma-separated sequence.
    
Ans

def pr(n):
    lst=[]
    
    for x in range(100,n+1):
        s=str(x)
        """Here str stands for String, and it should be used as same"""
        if(int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0):
        """Here we are taking the value with indexing: x=100 and indexing: [0]:1, [1]:0, [2]:0"""
            lst.append(x)
    print(lst,", ")
n=int(input("Enter the number: "))    
pr(n)  

13. Write a Python program to print alphabet pattern 'R'. Go to the editor
Expected Output:
    
x=10
if x<=10:
    print("****")
    if x<=10:
        print("*   *")
        if x<=10:
            print("*   *")
            if x<=10:
                print("*   *")
                if x<=10:
                    print("*****")
                    if x<=10:
                        print("**")
                        if x<=10:
                            print("* *")
                            if x<=10:
                                print("*  *")
                                if x<=10:
                                    print("*   *")
    
14. Write a Python program to check whether an alphabet is a vowel or consonant.
Ans
def fck(n):
    if set('aeiou').intersection(n.lower()):
        print("%s Alphabet is a "%(n),"vowal")
    elif set('123456789').intersection(n):
        print("%s is not an alphabet, please enter an alphabet: "%(n))
    else:
        print("constant")
    
n=input("Please Enter the Alphabet: ")
fck(n)

15.Write a Python program to convert month name to a number of days. Go to the editor
Expected Output:
List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days 

def Month(n):
    dict={'January':31,'February':'28/29',
          'March':31,'April':30,'May':31,
          'June':30,'July':31,
          'August':31,'September':30,
          'October':31,'November':30,
          'December':31}

    for x in dict:
        if x!=n:
            continue
        else:
            print(dict[x])
            break
n=input("Please enter the month name: ")
Month(n)
    
or

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name")
    

16.Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
Ans

def sum(n,m):
    a=n+m
    if (a)>=15 and (a)<=20:
        print(20)
    else:
        print(a)
n=int(input("Enter the first variable: "))
m=int(input("Enter the Seconf variable: "))        
sum(n,m)

or

def cv(a,b):
    
    c=a+b
    if c in range(15,21):
        print(20)
    else:
        print(c)
    
a=int(input())
b=int(input())
cv(a,b)

17.Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle 

Ans
def triangle(e,i,s):
    
    if e==i and i==s:
        print("Equilateral triangle")
    elif e==i or i==s:
        print("Isosceles tringle")
    else:
        print("Scalene triangle")
    
e=int(input("Please enter the value 1 : "))
i=int(input("Please enter the value 2 : "))
s=int(input("Please enter the value 3 : "))
triangle(e,i,s)

or


def triangle(m,n,o):
    if m==n==o:
        print("equilateral triangle")
    elif m!=n and n!=o and o!=m:
        print("scalene triangle")
    elif m==n or n==o or o==m:
        print("isosceles tringle")
            
m=int(input("Please enter the value 1 : "))
n=int(input("Please enter the value 2 : "))
o=int(input("Please enter the value 3 : "))
triangle(m,n,o)  

18.Write a Python program to calculate the sum and average of n integer
numbers (input from the user).
 Input 0 to finish.

Ans

def fun(a,b,c):
    
    c=a+b+c
    d=(a+b+c)/3
    
    print(c)
    print(d)
    
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
fun(a,b,c)


19.Write a Python program to create the multiplication table (from 1 to 10) of a number. Go to the editor
Expected Output:
    
Ans

x=6
while x<=6:
    y=1
    while y<=10:
        print(x,"*",y,"=",x*y)
        y+=1
    x+=1
print()

or

for x in range(6,7):
    for y in range(1,11):
        print(x,"*",y,"=",x*y)

20. Write a Python program to construct the following pattern, using a nested loop number. Go to the editor
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999

Ans.
def lp(n):
    for x in range(0,n+1):
        for y in range(0,x):
            print(x,end="")
        print()
n=int(input("Please input the value: "))
lp(n)

21.Print only the words that start with s in this sentence

st = 'Print only the words that start with s in this sentence'
for x in st.split():
    if x[0]=='s' or x[0]=='S':
        print(x)
        
or
st = 'Print only the words that start with s in this sentence'
[x for x in st.split() if x[0]=='s' or x[0]=='S']

Q22. if we have more then one list then we can use map: Since map combine all list to lists.
st = 'Print only the words that start with s in this sentence'
st_1 = 'This is a string which should be Split'
st_2 = 'String is nothing but a combination of char'
st_l = [st,st_1,st_2]

Ans
st = 'Print only the words that start with s in this sentence'
st_1 = 'This is a string which should be Split'
st_2 = 'String is nothing but a combination of char'
st_l = [st,st_1,st_2]
def start_split(st_l):
    for x in st_l.split():
        if x[0]=='s'or x[0]=='S':
            print(x)

list(map(start_split,st_l))
        
23.Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

list1=[x for x in range(1,50) if x%3==0]
list1

23.st = 'Print every word in this sentence that has an even number of letters'
st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
    l=len(x)
    if l%2==0:
        print(x,": is even")
    else:
        print(x,": is odd")
print()



    
        

    