    # -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:28:37 2020

@author: yamanish
"""

'''Starting of function:'''
=========================
We have 3 type of function:
    1) Build in Function: Len(), Print(), Count(), shuffle, randint, enumerate, min max, zip
    2) User defined Function: Which are defined by user.
    3) Anonymou's Function: lambda
=========================
So we are doing user defined function.
Q) How we define a function?
Ans By using DEF before the name of that function.
EX:
'''def add(enter the parameter like: x,y):'''
'''add(5,6): adding to values''' 

Q1) Make a formula to add variables.    

def add(x,y):
    c=x+y
    print(c)
add(5,6)
So we can call add any where at any time by entering the value.

Q) Why we need it?
Ans Bcz while doing a project we need to perform certain task and for avoiding to write the same code we create a function of that code.

--------------------
for ex:
def greet():
    print("Hello")
    print("welcome")
greet()

-------------------
#We can also return a value.
'''what is RETURN and what's its use.'''
Ans Return does not print a value however it gives a result as a total output and sane it.

Q) Use a formula to add 2 arguments and use Return function.

for ex:
def fun(x,y):
    c=x+y
    return c
fun(5,6)

or

def afs(x,y):
    c=x+y
    return c
result=afs(3,4)

'''here function does not return a value.'''

'''so here it just saved a value in c'''

def afs(x,y):
    c=x+y
    return c
result=afs(3,4)
print(result)

'''here function return a value'''

Q can we return 2 arguments?
Ans yes we can, use sum and sub

ex:
def afs_sub(x,y):
    a=x+y
    b=x-y
    return a,b
result1,result2=afs_sub(5,3)
print(result1,result2)


Q.  1)Define a function, user input his name.
    2)If the user name contain vowel than print "Your name contain vowals"
    3)In Result name should be printed in Series.


def name():
    name=input("Please enter the name: ")
    if set('aeiou').intersection(name.lower()):
        print('Your name contains vowal')
    else:
        print('Your name does not contain vowal')
    for x in name:
        print(x)  #This is used for series.
name()

Q Use a function range(0,20) but stop when it is equal's to 5.
So Ans should be
0
1
2
3
4
5
Ans

def loop_five():
    for x in range(0,20):
        print(x)
        if x==5:
            return
loop_five()

=========================
Factorial: 5!=5*4*3*2*1=120
=========================

def fact(n):
    y=1
    for i in range(1,n+1):
        y=y*i
    return y

result=fact(5)
print(result)

Concept of using y
Here y=1 and i is 1, so 1*1=y and now Y value is 1
Then i value is 2 and Y vale is 1(1*1), now Y*i(1*2)=3(Y)
Y*i(2*3)=Y(6)
Y*i(6*4)=Y(24)
Y*i(24*5)=Y(120) So that is the reason we have called Y.


=========================
Recursion function: Means calling a function itself.
=========================

Recursion basically means calling the same function in the function you created.

For ex:
def greet():
    print("Hello")
    greet()  #Here we have called this function in the same function.
greet() #Result an error
# The result will be infanite time print hello.

=========================
Recursive factorail function: Instead of using a Loop use Recursive function.
===========================

def fac(x):
    if x==1:       #This is used since factorial of 1 is 1 and we need more than that.
        return 1   #This is used so that it will not run infinity times.
    else:
        return (x*fac(x-1))  #6*6-1,6*5-1 and so on.
result=fac(6)
print(result)

or

def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x - 1))
num =int(input("Please enter the value: "))
print("The factorial of" , num , "is ", calc_factorial(num))

-----------------------------





======================
Arguments in Python
======================

Ther are 2 type of Arugument:
1) Formal argument:
    Ex: def sum(x,y) --> This is formal Argument.

2) Actual Argument:
    Ex: sum(6,7) --> While calling the value in the Arugment.

Now Actual argument are of 4 type:
    1) Poition Argument
    2) Keyword argument
    3) Default argument
    4) Variable Argument
    
Explain -

1) Position Argument:
   ------------------ 
    When the position of the argument is same while giving the perameter and calling the same.
 For ex:
     
def person(name,age):
    print(name)
    print(age)
person('manish',25)

Here the postion of manish and name is 1st.
Position od 25 and age is 2nd so it give the result however when we are not sure about position than what we can do.
For ex if we want to call person function however we are not sure where the name position is.

Ans So to resolve this problem, keyword Argument comes to our mind.

2) Keyword Argument:
--------------------
    We assign a key to our values at the time of calling.
For ex:
    
def person(name,age):
    print(name)
    print(age)
person(age=25,name='manish')

Here we have changed the position however assigned a key to the value.

3) Default Argument:
--------------------

Q Now the question arises that if we will not provide a value to an argument then what will happen.
Ans We can give a default value to an argument so that if we are not providing a value while calling an argument then even we will get it.

For ex: 

def person(name,age=25):
    print(name)
    print(age)
person('manish')


def profile_info(name,followers=1):
    print("username:",name)
    print("Followers:",followers)
profile_info("Manish")
profile_info(name='kapil',followers=235)

Q) if we change the age then what happen?
Ans: Yes we can change and it will provide the updated one.

def person(name,age=25):
    print(name)
    print(age)
person('manish',36)

4) Variable Argument:
---------------------

When we are not sure that how many arguments we need to enter in the function than we use this function.
So we want to eneter multiple argument in the function than we use this function.

1) Variable length argument          = *
2) Keyword variable length argument. = ** (*= Key, *= value)

So we can * and **kwargs
------------------------
1) use of *

def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
sum(23,36,75,45)

or single use of Argument

def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
sum(1,2,3,4,5,6)
-----------------
Try it with string and number

def sing(name,*b):
    print(name)
    print(b)
sing('mani',27,'xyz','70 kg')

So here in the result we have seen that, we have enter multiple argument: 27,'xyz','70 kg')
    However we are not sure what is 27, xyz or 70 kg.
 So to assign a key them so that we can understand that why we use it and what is this vale.
Here we use ** keyword variable length argument. 

-------------------


2) use of **kwargs
'Keyworded Variable Length Arguments in Python ,pass the mutiple keyword/data'

def detail(name,**kwargs):
    print(name)
    print(kwargs)
detail('manish',age=25,address='xyz',mob=9718)

'Now how to print them in a series and how to use it properly.

def detail1(name,**kwargs):
    print(name)
    for i,j in kwargs.items():
        print(i,j)
detail1('manish',age=25,address='xyz',mob=9718)

Q) How use this with input:
    
def detail(**b):
    n=input("enter the data")
detail(n)

Q)  Use a function to input how many arguments you need.
    Than make the user to input arguments.

def add(**b):
    a=int(input("Enter how many times u want to enter:"))
    for i in range(a):
        if i<=a:
            d=input("Enter the Details")
    for n,m in b.items():
        print(n,m)
add()

Q If a user use both *args and **kwargs

def n(*args,**kwargs):
    if 'Fruits' and 'Juice' in kwargs:
        print("I like: {} and in fruits i like to eat: {}".format(" , ".join(args),kwargs))
    else:
        pass
    
    
n('butter','egg',Fruits='Mango',Juice='Lichi')


=================================================
Scope
=================================================
Scope are of 2 type:
    1) Global
    2) Local

Global: When variables are declared outside the function and can be used anywhere in the function than it is called Global

Local: When variables are declared inside the function than these are called local.

Q Is it possible to use 2 variable in the same code.
Ans. Yes
Ex:

a=10 #Global Var   
def AKG():
    a=15 #Local Var
    print("In fun ",a)
AKG()
print("Out funct ",a)    

Q can we use the Global var inside the function or call it inside a function.
Ans yes we can

'for ex':
    
    a=10
    def AKG():
        print("inside",a)
    AKG()
    print("outside",a)

Q can we update/change the value of Global variable in the function.
Ans Yes we can do that by changing the value by using global before variable.
or
Q can we convert a local variable into a global
Ans. Yes we can do it by using global before the variable.

'for ex':
    
    a=10
    def AKG():
        global a
        a=15
        print("inside",a)
    AKG()
    print("outside",a)

#Here we dont have a local var.

QCan we change the value into a list:
    
Ans

    a=10
    def AKG():
        global a
        a=[1,2,3,4,5,6,7]
        print("inside",a)
    AKG()
    print("outside",a)

Q can we use local variable outside a function.
And. No we cannot use.


Q can we update a value of golbal var. and also use a local var with the same name.
Yes we can do this with the help of Globals
#main part: x = globals()['a']
            #globals()['a'] = 15

For Ex:
    a=10
    def AKG():
        a=9  #Local
        print("inside",a)
        x = globals()['a']
        globals()['a'] = 15 #[here we have not used x=15 bcz it means a new var is created whose value is 15]
    AKG()
    print(a)
    
    or we can use different variable name for local and global
    
    x=10
    def AKG1():
        
        a=9 #local
        print("Inside",a)
        
        global x
        x=x+10
               
    AKG1()
    print("Outside",x)
    
========================
Fibonacci Sequence: 
=======================
0
1
1
2
3
5
8
13
21
#Here is a patten that first no + second No.
#than 2nd no with 3rd no. ans so on.

def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        for i in range(2,n):
            c=a+b
            a=b  #Here we are just swapping a with b and b with c.
            b=c
            print(c)
    
fib(10)


--------------------------------------------
        
Q1) How to use a list in the function and provide the no of Odd and Even?

def count(lst):
    
    even=0
    odd=0
    
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[23,23,4,5,6,3,2,2,4,32,5,6,6,33]
even,odd=count(lst)
print(even)
print(odd)

-------------------------------------------

list=[]
c=int(input("enter the details"))
for i in range(c):
    if i<=c:
        data=input()
        list.append(data)
        print(list)
        
===============================================================================

This is 3rd function in Python:
    Anonymou's Function.

No need to define variables
Automatically iteration
No need to return
No parameters.


lambda
===============================================================================

1)Multiplication

f=lambda a: a*a
result=f(4)
print(result)

2) Add

f=lambda a,b: a+b
result=f(2,3)
print(result)

3)Substract

f=lambda a,b: a-b
result=f(5,2)
print(result)

4)Exponent

f=lambda a: a**4
result=f(5)
print(result)
------------------

===============
lambda has 3 function:
    1)filter()
    2)map()
    3)reduce()

    These 3 are basically used to 1st filter the data and than map(change as per our need) and than reduce it to single result. 
==============
1) Filter : It takes 2 Arguments: 1st one is function/logic and 2nd is list/sequence.

'lambda use'
'''def is_even(n):
    if n%2==0:
        return n
        or
    return n%2==0
nums=[3,2,6,8,10,11,13]
evens=list(filter(is_even,nums))
print(evens)'''

nums=[3,2,6,8,10,11,13]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)

------------------
2) Map : It means change the value by doing an operation.
    It takes 2 Arguments: 1st one is function/logic and 2nd is list/sequence/iteration.
    
"""Always Remember that for using REDUCE we have import thsi function:
    --FROM FUNCTOOLS IMPORT REDUCE--"""

 '''def update(n):
    return n*2
nums=[3,2,6,8,10,11,13]
evens=list(filter(is_even,nums))
double=list(map(update,evens))
print(double)''' 

num=[3,2,5,6,7,89,456,345]
evens=list(filter(lambda n: n%2==0,num))
double=list(map(lambda n: n*2,evens))
print(double)  
----------------------
3) Reduce: It help in getting a result form the map list
    We can onlu use by doing the below operation.

from functools import reduce

'''def sum_all(n,b):
    return n+b
from funtools import return

num=[2,3,4,5,6,7,8,9,6,6,5,5,45,4,4,4,2342,4,3,3,322,234]
even=list(filter(lambda n: n%2==0,num))
double=list(map(lambda n: n*2,num))
sum=reduce(sum_all,double)
print(sum)'''

from functools import reduce
num=[2,3,4,5,6,7,8,9,6,6,5,5,45,4,4,4,2342,4,3,3,322,234]
even=list(filter(lambda n: n%2==0,num))
double=list(map(lambda n: n*2, num))
sum=reduce(lambda n,m: n+m,num)
print(sum)

or

from functools import reduce

nums=[3,2,6,8,10,11,13]
even=list(filter(lambda a:a%2==0,nums))
print(even)
double=list(map(lambda a:a*2,even))
print(double)
sum=reduce(lambda a,b: a+b,double)
print(sum)

=========================================================================================================================
Decoraters
=========================================================================================================================

Decorators can be thought of as functions which modify the functionality of another function.
They help to make your code shorter and more "Pythonic".

Decoraters basically follows Scope(Global and Local).

In python eveything is a object so a function is also an object and can be used inside another function.

------------------------------------
***IMP : when we use parentheses ()

def hello(name):
    return 'Hello '+name
hello('John') #here we have used () because we are calling the function.

So we call a function then we use parenthese and when we assign a function to a variable then not.

greet=hello

greet '''when we call without parenthese then it will direct us towards "<function __main__.hello>"'''

greet() '''it will give us the result'''


Now what happen we delete hello function?
Ans Even though we deleted the name hello, the name greet still points to our original function object.
    It is important to know that functions are objects that can be passed to other objects!
-----------------------------------

Functions within functions
Great! So we've seen how we can treat functions as objects, now let's see how we can define functions inside of other functions:

Ex1.

def hello(name):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"

    greet()
hello('josh')

Ans if we exicute the above function: The hello() function has been executed
So if we are calling greet without print it is not working.
************
Ex2. use of greet with print

def hello(name):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
hello('josh')

Ans for the above function: The hello() function has been executed
         This is inside the greet() function
         
So here we have seen that when we use a function inside a function then we have to use print while calling that.

********AND WE CANNOT RUN GREET AND WELCOME INDIPENDENTLY WITHOUT MAIN FUNCTION HELLO.

************
Ex3.

def hello(name):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
hello('josh')

Now the problem is if we exicute the function hello both function work and we need it to run as per the situation.

----------------------
with return statement:
----------------------

def hello(name):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    if name=='josh':
        return greet()
    else:
        return welcome()
hello('sam')

-----------------------
Functions as Arguments
-----------------------

def hello():
    return 'Hi josh'

def other(fun):
    print('other code would go there')
    print(fun())
    
other(hello)

-----------------------
How to create Decorator
-----------------------

def new_decorator(func):
    
    def wrap_func():
        print("Code would be here, before executing the func")
        
        func()
        
        print("Code here will execute after the func()")
    return wrap_func

def func_need_decorator():
    print("This function is in need of a Decorator")
    
func_need_decorator=new_decorator(func_need_decorator)

func_need_decorator()

or

def new(fun):
    
    def wrap():
        print('inside wrap')
        
        fun()
        
        print('outside wrap')
    return wrap

def new_fun():
    print('gift')
    
new_fun=new(new_fun)

new1()
*****************
So an alternative way of doing that is: @

@new_decorator
def func_need_decorator():
    print("This function is in need of a Decorator")
func_need_decorator()


Q) When we enters a number for division. The numerator should be bigger than the denominator.
    Even if num is enter smaller.

def div(a,b):
    if a<b:
        a,b=b,a
        print(a/b)
#Here the problem is Num is less and den is more.
div(5,6)

So the problem is when you don't have the code or you do not want to change the function.
Ans Than Decorator comes to the picture.


'Decorators'

def div(a,b):
    print(a/b)
#here we are creating a new function as decorative or add on.
def smart_div(func):
    def inner (a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1=smart_div(div)
div1(2,4)

==========================================================================
Questions for Function.
==========================================================================

This is an example of using Function in other function.

1. Write a Python function to find the Max of three numbers.
Ans

def max_of_two(x,y):
    if x>y:
        return x
    else:
        return y
def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))

x=int(input("Please enter the 1st value: "))
y=int(input("Please enter the 2nd value: "))
z=int(input("Please enter the 3rd value: "))
print(max_of_three(x,y,z))

#Here the consept we have use is:
Step 1. max_of_two(y,z) : max_of_two(8,-10)
Step 2. max_of_two(x,(result from previous: Y)) : max_of_two(2,8): 8
So Y = 8 and we get Max value.

"""We create a function and than we use that function in other function"""
"""We have used bracket concept: First Inner bracket will give result: (y,z):(8,10)"""
"""Now by using first formula we get a result of Y and now same will be applied to outer formula between (x,result:Y)
    (2,8)= 8"""
    
2. Write a Python function to sum all the numbers in a list.
Ans

def sum(n):
    total=0
    for x in n:
        total+=x
    return total
    
print(sum((8,7,3,4,0,9)))

or

def manish(n):
    a=0
    for x in n:
       a+=x
    return a
n=[1,2,3,4,5,56,6,7]
manish(n)

    3. Write a Python function to multiply all the numbers in a list. 
Ans

def Mult(n):
    a=1
    for x in n:
        a*=x
    return a

print(Mult((8, 2, 3, -1, 7)))

or

def manish(n):
    a=1
    for x in n:
        a*=x
    return a
n=[2,3,4,5,6]
manish(n)

4. Write a Python program to reverse a string?
Ans

def reverse_string(str1):
    rvstr1=''
    index=len(str1)
    """Here we have taken length of str in Index"""
    while index>0:
        rvstr1+=str1[index-1]
        """when we use indexing we need result of 3 position then we write: print(list[3])"""
        """In the same wayn we are using indexing where we need print(n[7]): 7th Position"""
        """This will give a result of 7 which we are using as Indexing=0,1,2,3,4,5,6,7"""
        index=index-1
    return rvstr1
print(reverse_string('abcd1234'))

or

def rev1(n):
    rev2=''
    index=len(n)
    while index>0:
        rev2+=n[index-1]
        index=index-1
    return rev2
n=input("Please enter a string: ")
rev1(n)

5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
Ans

def fac(n):
    if n==1:
        return 1
    else:
        #for x in range(2,n+1):
        #   y=y*x
        #return y
        return (n*fac(n-1))
n=int(input("Enter the value of Factorial: "))
result=fac(n)
print(result)

6. Write a Python function to check whether a number is in a given range.
Ans

def test(n):
    if n in range(3,9):
        print("number %s is in the range"%str(n))
        """ Use of %s: We can use this where we want to print the value and then at last declare the source: %str(n)"""
    else:
        print("Number is not in the list")

test(6)

7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

Ans

def test_string(n):
    d={'UPPER CASE':0, 'lower case':0}
    for x in n:
        if x.isupper():
            d['UPPER CASE']+=1
        elif x.islower():
            d['lower case']+=1
        else:
            pass
    print("Original string is: ",n)
    print("No of upper case: ",d['UPPER CASE'])
    print("No of lower case: ",d['lower case'])

test_string('The quick BrowseR Fox')

or
Q)Tell: 'The Kapil SharMA ShoW'

def tes(n):
    a=0
    b=0
    for x in n:
        if x.isupper():
            a+=1
        elif x.islower():
            b+=1
        else:
            pass
    print("Original String:",n)
    print("No. of Upper case characters :",a)
    print("No. of lower case characters :",b)

n=input("Please enter the String: ")
tes(n)


8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]


def old_lst(n):
    new_lst=[]
    for x in n:
        if x not in new_lst:
            new_lst.append(x)
    print(new_lst)
    
n=[1,2,3,3,3,3,4,5]    
sample(n)
===============

if want the user to input than input should be like a string without comma:
    
def old(n):
    
    lst=[]
    for x in n:
        if x not in lst:
            lst.append(x)
    print("New list is: ",lst)
    
n=input()
old(n)

9. Write a Python function that takes a number as a parameter and check the number is prime or not?
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

Ans
**In this question we have to keep in mind that : No even number is prime 
so we are dividing it with 3.

import math

def pr(num):
    
    if num%2==0 and num>2:
        return False
    for i in range(3,int(math.sqrt(num))+1,2):
        '''Why we use this range: it is doing range(start (3): stop: step(2))
        then we have: math.sqrt(num)+1: It means we are taking the square root of like(100): 10.
        So 10+1 = 11
        So this means: range(3,math.sqrt(num)+1,2)
        num= 100
        range(3,11,2)'''
        
        if num%i==0:
            return False
        return True
num=int(input("Please enter the value: "))
pr(num)




or

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
            """This means till if we will get just one 0 as a remainder that means it is divisible by other no. and not a prime"""
            """secondly we have not included 1 """
                return False
            else:
                return True             
print(test_prime(9))

or: if negative value or zero is input then
we can also use absolute: num=abs(num) for negative values.

def prime(n):
    
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        for x in range(2,n):
            if n%x==0:
                return False
            else:
                return True
            

n=int(input("Please enter the value: "))
prime(n)

10. Write a Python program to print the even numbers from a given list. Go to the editor
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]

Ans

num=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even=list(filter(lambda a: a%2==0,num))
print(even)

or

def even(n):
    lst=[]
    for x in n:
        if x%2==0:
            lst.append(x)
    return lst
n=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even(n))

11. Write a Python function to check whether a number is perfect or not. Go to the editor
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal 
to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding 
the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number 
that is half the sum of al  l of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors,
and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all 
its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
 This is followed by the perfect numbers 496 and 8128.

Ans

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))


12. Write a Python function that checks whether a passed string is palindrome or not.

def poli(n):
    n=input("Enter the String: ")
    if n==n[::-1]:
def perfect(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum+=x
    return sum==n
        print("True")
    else:
        print("False")
poli(n)

13.Write a Python function to check whether a string is a pangram or not. Go to the editor
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Ans

"""string.ascii_lowercase or uppercase is used for ('abcdefghijklmnopqrstuvqxyz')"""
"""to use string we have import string"""
import string
def Pangrams(n,alphabets=string.ascii_lowercase):
    alphaset=set(alphabets)
    return alphaset<=set(n.lower())
    
Pangrams("The quick brown fox jumps over the lazy dog")

14. Write a Python function to create and
 print a list where the values are square of numbers between 1 and 30 (both included).
 
 Ans
 
 def square():
     list=[]
     for x in range(1,31):
         x=x**2
         list.append(x)
     return list
     
print(square())

15. Check weather a Integer is a Palindrome or not?
Ans

def pali(n):
    
    original1=n
    reverse1=0
    
    while n>0:
        d = original1 % 10
        reverse1 = reverse1*10 + d
        n = n//10
    if original1==reverse1:
        print("yes")
    else:
        print("no")
    
    
n=int(input("Please enter the no : "))
pali(n)

16. Write a function that returns the number of prime numbers that exist up to and including a given number

for num in range(2,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)
       
or

def prime(n):
    lst=[]
    for x in range(2,n+1):
        if x%2==0 or x%3==0 or x%5==0:
            continue
        else:
            lst.append(x)
            
    print(lst)   

n=int(input("Please enter the value: "))
prime(n)

17. Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
lesser_of_two_evens(2,3)    


18.
Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False

def m(a,b):
    
    if a+b==20:
        return True
    elif a==20 or b==20:
        return True
    else:
        return False
    
a=int(input())
b=int(input())
m(a,b) 

19.

***This is Important: How we can use" f,s = text.split(" ") " to getb the data from the same string with different words

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

or

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
animal_crackers('Levelheaded Llama')

20.
***IMP

Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
 
 
def spygame1(n):
    
    return '007' in ''.join(str(i) for i in n)
    
spygame1([1,2,4,0,0,7,5])

21.
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

def check1(n):
    
    return '33' in "".join(str(i) for i in n)
    
n=[3, 3, 3]
check1(n)

22.Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
makes_twenty(20,10)

23.
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
old_macdonald('macdonald')


24.
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
    while not add:
        if num != 9:
            break
        else:
            add = True
            break
    return total
summer_69([4, 5, 6, 7, 8, 9])

25.
Guessing Game Challenge
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!

Ans

def Game():
    
    print("Here are the rules: \n'Guess a number between 1 and 100.' \n 'Hint will be provided if required.'")
    
    from random import randint
    Random_no=randint(0,100)
    Random_no1=Random_no-10
    Random_no2=Random_no+10
    print(Random_no)
    
    Guess=int(input("Please try a no: "))
    
    if Guess==Random_no:
        print("WOW Correctly Guessed the number :",Guess)    
    
    elif Guess >= Random_no1 and Guess <= Random_no2:
        print("WARM")
    else:
        print("COLD")
    previous = Guess
    
    guess_list=int(1)
    
    while Guess!=Random_no:
        guess_list=guess_list+1
        Guess=int(input("Try again! "))
        if Guess==Random_no:
            print("Now you guessed the correct no %s"%(Guess))
            print("You took %s chances"%(guess_list))
            break
        
        if Guess<0 or Guess>100:
            print("Out of Bounds, try again")
            break
            
        current = abs(Guess-Random_no)
        old = abs(previous-Random_no)
        
        if current <= old:
            print("Warmer: You are closer to the number" )
        else:
            print("Colder: You number is further away from the previous number")
        previous=Guess
        
Game()






