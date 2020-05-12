# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:17:14 2020

@author: yamanish
"""

Whats is OOP's?
Ans Object oriented Programming

Why we use OOPS?
Ans We learn OOPs to create our own OBJECTS and perform some function with the object.

OOPS have class

What is a class?
Ans Class is a blueprint of the final Object.
In class we basically define complete behaviour of the object.

Under class we have 2 thing: 1. Attributes 2. Methods

Q) What is Instance Method?
Ans When a function is defined inside a class is called a Instance Method.

Attributes = Variables (which are common to all):(Age,name,Height,color)
It means all human will have some age, name, height, color. However these attributes were different
but they have it. So attributes are common.

Method = Function = Behaviour:
    Basically the function created under a class is called Method.

So we define methods under classes.

Q) How to define a class?
Ans

'''we define class by "CLASS Keyword" and the first(1st) word of the class name should be CAPITAL.'''
class Person():
    '''#How to initialize attribute
    #To initilize attribute we use "__init__ method
    #We define Methods like Functions with "DEF"
    #When ever we define a method in a class always use SELF as the "1st Argument".'''
    def __init__(self,name,age,weight,height):
        self.name=name       '''Object.name=name'''     
        self.age=age         '''Object.age=age'''          ------------->  These are called Instance Variable.
        self.weight=weight   '''Object.weight=weight'''                  Since we can change these variable in class.
        self.height=height   '''object.height=height'''

'''Now we will define the Object name and equal's that with class name'''
'''Object = Instance'''
Person1 = Person('manish',25,"74 = KG","175 cm")
'''when we define a object than it call init method, than self = object.'''
'''In Simple words self represent OBJECT'''

print(Person1.name)

'''we can create as many onjects we want like below'''
Person2 = Person("Rohit",26,"75 Kg","170 cm")
print(Person2.age)
---------------------

Q) Now Question is what is constructor?
Ans Like when we create an Object -- call __init__ method -- it create a space for object to do some work.
    So instead of using the name init method we can call it Constructor.
----------------------
    
Q) What is Instance Variable and What is Class Variable?
Ans. So in class we have 2 Variables: 1. Instance Variable and 2. Class/Static Variable.
1. Instance Variables : These are the variables which are defined inside __init__ in a class and only affect an Object.
    
2. Class Variable : These are the variable which are defined outside __init__ in a class and affect all the Object.
In simple way we can say that a common variable which is common to all objects than it will affect all the objects.
    
For ex make a class for car and in that show a class Var and a instance Var.



class Car():
    #Here we use class Variable which will affect all the OBject and they are common to all Objects.
    #wheels are common to all the cars.
    wheels = 4 # we can call them while printing
    #How we call it "Object.wheels" inisde print.
    #we can also change the value of the wheel in the class.
    #How we can do it. Ans. car.wheels = 5.
    
    def __init__(self):
        self.brand="BMW" # This will be changed as per Object
        self.engine="WW"
        self.cc="2000 CC"
        #These above variables are called Instance Variable and can be changed for an Object.

C1 = Car()
C2 = Car()

Car.wheels = 5

print(C1.brand,C1.cc,C1.wheels)

#Now we can change the CC of C2
C2.cc = "2500 CC"
C2.brand = "Honda"

#So here we have changed the variable for C2 however it has not affcted the value of other object.
#This is called a Instance Variable.

print(C2.brand,C2.cc,C2.wheels)        


-----------------------   
Q) Now make a class programe? and can we change the variable value after defining the value to the argument.
Ans.
    
class Person():
    
    def __init__(self,name,weight,age,height):
        self.name=name
        self.weight=weight
        self.age=age
        self.height=height

person1 = Person("Manish","75 Kg",25,"175 cm")
person1.age=30
print(person1.age)  #we can change the age of the person1

person2 = Person("Rohit","70 Kg",26,"170 cm") 
print(person2.age) 


   
Q) Create a class for computer in which you will pass 2 arguments Ram and CPU?
Ans.

class Computer():
    
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        
HP= Computer("i7","8 gb")
Asus= Computer("i8","12 gb")
print(HP.ram)
print(Asus.cpu)

Q) Create a class in which make a function for Area of rectangle?

class Geometry:
    def __init__(self,width, height):
        self.width = width
        self.height = height
        #self.color = color
    
    def rectangle(self):
        return self.width* self.height
    
#    def rec_color(self):
#        pass

a = int(input("Enter width: "))
b = int(input("Enter height: "))
obj = Geometry(a,b)
print("ARea: ",obj.rectangle())

======================
Method
======================

Q) How many type of method we have?
Ans 
    We have 3 type of method:
        1) Instance method: They are used with instance variable: use(self)
        2) Class method: They are used with Class variable: use(cls)
        3) Static method: When don't want to use a class or instance variable. Something different than we use this variable. 
            use:(): if u dont want to use any variable.
    
1) Instance: When we define a function under a class than it is called Instance method.
   
   It has 2 type:1)Accessor Method: If you just want to fetch the value, called Accessor.
                    @ we use get_(variable name) to get the value by defining the method.
                   
                2)Mutators Method: If you want to change the value, called Mutators.
                    @ We use set_ to set the value by changing the value.

2) Class method: They are used with Class variable: use(cls)
    for using a class method we have to use decorators: @classmethod   
                 
3) Static method: To use this method : use()
    for using a static method we have to use decorators: @staticmethod

Example of the above Method:
Q Make a classin which we can enter the numbers for different subject
Instance Method: Function Average of numbers.
Class Method : Function to get the name of the School
Static Method: This class is for what.

Ans


class Student:
    
    """Class Variable"""
    school="Manish School"
    
    """Below are the attributes and INSTANCE VARIABLE"""
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
   
    
    
    """Instance Method"""
    """In INSTANCE METHOD WE USE Self"""
    """INSTANCE Method is used with INSTANCE VARIABLE"""
    def avr(self):
        return (self.m1+self.m2+self.m3)/3
    
    
    """Class Method""" 
    """Classmethod is a decorater to use class method"""
    """In Class Method we use Cls"""
    """Class method is used with Class Variable"""
    @classmethod
    def school_name(cls):
        return cls.school
    
    
    """Static Method"""
    """This is used when we do not use Class or Instance"""
    """With static var we use def name(blank)"""
    """We need to use Decoratoe: @staticmethod"""
    @staticmethod
    def info():
        print("This is for student class")
    
    
    
    
s1 = Student(23,45,65)
print(s1.m1)
s2 = Student(12,35,67)
print(s2.m2)

"""How to call Instance Method """
s1.avr()

"""How to call Class Method"""
"""Here we can use a class name: Student.school_name()"""
s1.school_name()

"""How to call static Method"""
"""We can also use s1.info()"""
Student.info()
-----------------------
code:
    
class Student():
    
    school="Manish"
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avr(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def school_name(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is a student class")
            
s1=Student(23,45,65)
s1.avr()

s1.school_name()
s1.info()



Q) How to use get and set method in Class?
    Also using Instance Method.
    
Ans

class Prnt():
    
    def __init__(self):
        self.str=" "
        
    def get_str(self):
        self.str=input("Enter the String: ")
        
    def set_str(self):
        print(self.str.upper())
str1=Prnt()
str1.get_str()
str1.set_str()
------------------------------------------------
Q) How to reverse a sentence?
    Ex:    "hello .py""
    Result:".py hello
        
class Rev():
    def rev_word(self,n):
        return ' '.join(reversed(n.split()))
    '''This line is working:
        1) n.split will split all the words: 'h' 'e' 'l' 'l' 'o'
        2) then Reversed will reverse all the words: 'o' 'l' 'l' 'e' 'h'
        3) then Join is helpng in joining all the words'''

print(Rev().rev_word("hello .py"))
--------------------------------------------------

Q) How to create a Class under a Class and what we call it?

Ans So Class in class is called : Inner class.
    We need it when we want to perform some activity for only this class.
    
Q) Create a class for students and then create an inner class of Laptop.
    
Ans

class Student():
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        """Here we are declaring the inner class"""
        self.Lap=self.Laptop()
        
    def show(self):
        print(self.name,self.rollno)
        self.Lap.show()
    
    """Here we have created an inner class which is specific to STUDENT Class"""    
    class Laptop():
        
        """We have to declare this class in the main class: self.lap=self.Laptop"""
        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i7'
            self.ram = 8
            
        def show(self):
            print(self.brand,self.cpu,self.ram)
            
        
stu1=Student('Manish',2)
stu2=Student('Kapil',3)

"""This show is for name and roll no"""
stu1.show()

or
"""This show is for Laptop"""
"""stu1.Lap.show()"""
------------------------------------
class Student():
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.Lap=self.Laptop()
        
    def call(self):
        print(self.name,",",self.rollno)
        self.Lap.call()
    class Laptop():
        
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8
        
        def call(self):
            print(self.brand,self.cpu,self.ram)
        
stu1=Student('Manish',2)
stu1.call()

--------------------------------------------------
Q) Features of OOP's?
Ans
    Four features of OOP's:
        1) Inheritance
        2) Abstraction
        3) Polymorphism
        4) Encapsulation
    
1) Inheritance: It is divided into 4 parts:
    
    1) Single Level inheritance
    2) Multi level inheritance
    3) Mulitiple inheritance.
    4) Hierachical inheritance

1) Single: In single level inheritance one is the Super class and other is the Sub class.
            It is like a Parent <<<======  Child relation.
            Whatever is within a Super class, will get in child/Sub class.
            
Ex:

    Super class    : We will have class in that we have 2 Feature.
    Child/Sub class: We will have another 2 features.

Q how to use the Super class features in the sub class.

Ans

class F():
    
    def feature1(self):
        print("Feature1 working in F")
        
    def feature2(self):
        print("Feature2 working in F")
        
"""Now we are creating a new class and use above class feature int."""

class G(F):
    
    def feature3(self):
        print("Feature3 working in G")
        
    def feature4(self):
        print("Feature4 working in G")


A1= F()
A1.feature1()

"""Here we are using the function of F in G."""
B1= G()
B1.feature2()

      

--------------------------------------
--------------------------------------

2) Multi level inheritance: In this we have one is the Super class and other is the Sub class and than we have Sub class.
            It is like a Grand Parent <<=== Parent <<==== Child relation.
            Whatever is within a Super class, will get in child/Sub class and than sun child class.

Ans:
    
class F():
    
    
    def feature1(self):
        print("Feature1 working in F")
        
    def feature2(self):
        print("Feature2 working in F")
        
"""Now we are creating a new class and use above class feature int."""

class G(F):
    
    def feature3(self):
        print("Feature3 working in G")
        
    def feature4(self):
        print("Feature4 working in G")
        
class H(G):
        
    def feature5(self):
        print("Feature5 working in H")
        
    def feature6(self):
        print("Feature6 working in H")


A1= F()
A1.feature1()

"""Here we are using the function of F in G."""
B1= G()
B1.feature2()

"""Here we are using the function of Super class and sub class"""
C1= H()
C1.feature2()
C1.feature4()

=========================================
Example of Hierachical inheritance:
========================================    

class School_member():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def basic(self):
        print("Name : {}, Age : {}".format(self.name,self.age)," , ",end="")
        
class Student(School_member):
    
    def __init__(self,name,age,marks):
        School_member.__init__(self,name,age)
        self.marks=marks
        
    def student_detail(self):
        School_member.basic(self)
        print("Marks : {}".format(self.marks))
        
class Teacher(School_member):
    
    def __init__(self,name,age,salary):
        School_member.__init__(self,name,age)
        self.salary=salary
        
    def teacher_detail(self):
        School_member.basic(self)
        print("Salary : {}".format(self.salary))
                
s1=Student('Manish',25,99)
s1.student_detail()

t1=Teacher('Manish',25,100000)
t1.teacher_detail()

s1=Student('Manish',25,99)
t1=Teacher('Manish',25,100000)
members=(t1,s1)

for member in members:
    print(member)
    
or we can change the student_detail and teacher_detail to call:

for member in members:
    member.call()
--------------------
Q) Make a Hierachical inheritance for Company:
    
class Company():
    
    def __init__(self,name,age,post):
        self.name=name
        self.age=age
        self.post=post
        
    def call(self):
        print('Name:"{0}", Age:"{1}", Post:"{2}"'.format(self.name,self.age,self.post),",",end="")
        
class Employer(Company):
    
    def __init__(self,name,age,post,turnover):
        Company.__init__(self,name,age,post)
        self.turnover=turnover
        
    def call(self):
        Company.call(self)
        print('Turnover:"{0}"'.format(self.turnover))
        
class Employee(Company):
    
    def __init__(self,name,age,post,salary):
        Company.__init__(self,name,age,post)
        self.salary=salary
        
    def call(self):
        Company.call(self)
        print('Salary:"{0}"'.format(self.salary))
        
e1=Employer('Manish',45,'Head',200000000)
e2=Employee('Suresh',24,'Manager',50000)

Members=(e1,e2)

for Member in Members:
    Member.call()
    
============================================================================================
Q) Multi Level Inheritance question:
============================================================================================    

    Super class: (User input) Create a class of students where we need: name, age and gender
    Sub class: (User Input) create marks class
    SUB class: using super class and sub class add the no of child and give result.
    
Desired result:
    Enter the marks for your first three tests:

Test1: 90

Test2: 98

Test3: 99
=====Printing Student Details========
manish
25
Male
====PRINTING YOUR TEST SCORES==
90
98
99


Name:  manish
Age:  25
Gender:  Male
Total Marks:  287

Ans

class Student():
    
    def __init__(self):
        self.name=input("Please enter your name: ")
        self.age=int(input("Please enter your age: "))
        self.gender=input("Please enter your gender: ")
        
    def student_detail(self):
        print("Please enter your details: ")
        print(self.name)
        print(self.age)
        print(self.gender)
        
class Marks(Student):
    
    def __init__(self):
        super(Marks,self).__init__()
        print("================Please enter the marks of 3 Subjects: ============")
        self.test1=int(input("Hindi: "))
        self.test2=int(input("Maths: "))
        self.test3=int(input("English: "))
    
"""It is not necessary to print the below code since we are calling the last class
and not printing this data, so we can also avoid these codes"""
    def students_marks(self):
        print(self.test1)
        print(self.test2)
        print(self.test3)

class Total(Marks):
    
    def __init__(self):
        super(Total,self).__init__()
        self.total=self.test1+self.test2+self.test3
    

"""It is not necessary to print the below code since we are calling the last class
and not printing this data, so we can also avoid these codes"""

    def result(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Total Marks: ",self.total)
        
if __name__ == "__main__" :
    
    s1=Total()
    #s1.student_detail()
    #s1.students_marks()
    s1.result()

******
or
******

class Student():
    
    def __init__(self):
        self.name=input("Name:")
        self.age=int(input("Age: "))
        self.gender=input("Gender: ")
        
    def detail(self):
        print("======Printing the detail of the student======")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        
class Marks(Student):
    
    def __init__(self):
        super(Marks,self).__init__()
        self.m1=int(input("Hindi: "))
        self.m2=int(input("English: "))
        self.m3=int(input("Maths: "))
        
    def marks_obtained(self):
        print("===Printing the Marks of Student=====")
        print("Student got marks in Hindi: ",self.m1)
        print("Student got marks in English: ",self.m2)
        print("Student got marks in Maths: ",self.m3)
        
class Full(Marks):
    
    def __init__(self):
        super(Full,self).__init__()
        self.total=self.m1+self.m2+self.m3
        
    def fulldetail(self):
        Student.detail(self)
        Marks.marks_obtained(self)
        print("Total marks: ",self.total)

if __name__ == "__main__":
    s1=Full()
    s1.fulldetail()

==============================================
Multiple Inheritance
=============================================



3) Mulitiple inheritance: This is a senerio where A and B have no relation (Grand Parent and Parent have no relation)
    However C ( Child ) have relationship with both.
    
    [F]    [G]  
      \     /
       \   /
        \ /
        [H]: H is having relation with both of them.
        

Ex: 

class A():

    def feature1(self):
        print("This is the 1 Feature")
        
    def feature2(self):
        print("This is the 2 Feature")


class B():
    
    def feature3(self):
        print("This is the 3 Feature")
        
    def feature4(self):
        print("This is the 4 Feature")

class C(A,B):
    
    def feature5(self):
        print("This is the 5 Feature")
        
    def feature6(self):
        print("This is the 6 Feature")

a1= A()
a1.feature1()

b1=B()
b1.feature4()

"""Here C can also featch data for A and B"""
"""It is bcz it has relation with both A and B"""
c1=C()
c1.feature1()
c1.feature4

--------------------------
Q) Example of multiple inheritance:
   1)create a class of student with common feature
   2) create another class for detail with new features
   3) create 3 class and use the above 2 classes feature in the last class.
    
Ans:
    
class Student():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def call(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Detail():
    
    def __init__(self,rollno):
        self.rollno=rollno
        
    def call_detail(self):
        print("Rollno: ",self.rollno)
        
class Full_detail(Student,Detail):
    
    def __init__(self,name,age,rollno,subject):
        Student.__init__(self,name,age)
        Detail.__init__(self,rollno)
        self.subject=subject
        
    def get_full_detail(self):
        Student.call(self)
        Detail.call_detail(self)
        print("Subject: ",self.subject)

name=input("Please enter the name: ")
age=int(input("Please enter the age: "))
rollno=int(input("Please enter the rollno: "))
subject=input("Please enter the subject name: ")


s1=Full_detail(name,age,rollno,subject)
s1.get_full_detail()



-------------------------------------------

Q1) How Constrcutor behave in Inheritance
Q2) How to use super() in inheritance
Q3) Method Resolution Order.

Q) Now in inheritance how we can use Constructor(__init__)?
    
Q) What is method resolution Order? (MRO)
    
Ans.

class A():

    def __init__(self):
        print("this is __init__ of A")
        
    def feature1(self):
        print("This is A Feature")
        
class B(A):
    """BCZ we have linked A with B so we can call __INIT__ of A."""
        
    def feature2(self):
        print("This is B feature")
        
b1=B()
"""How it is calling the constructure of A bcz B can access all the feature of A.
Also B have no constructure so it will print the __init of A"""

Q) If B has its own constructure than?
Ans Than it will call B __INIT__ instead of A.

class A():

    def __init__(self):
        print("this is __init__ of A")
        
    def feature1(self):
        print("This is A Feature")
        
class B(A):
    """BCZ we have linked A with B so we can call __INIT__ of A."""
    def __init__(self):
        print("This is B __INIT__")
        
    def feature2(self):
        print("This is B feature")
        
b1=B()

Q) Now can we call __init__ of A by calling B __init__ ?
Ans We can do it with the help "Super" : it will reflect us to the super class.

Ex:
    
class A():

    def __init__(self):
        print("this is __init__ of A")
        
    def feature1(self):
        print("This is A Feature")
        
class B(A):
    """BCZ we have linked A with B so we can call __INIT__ of A."""
    def __init__(self):
        """Super help in fetching the init method"""
        super().__init__()
        print("This is B __INIT__")
        
    def feature2(self):
        print("This is B feature")

b1=B()

Q) But if we have another Class name C and then what will happen?
    Here we will do the question, What is method resolution Order? (MRO)

Ans
class A():

    def __init__(self):
        print("this is __init__ of A")
        
    def feature1(self):
        print("This is A Feature")
     
         
class B():
    """Here A and B are not inter related"""
    
    def __init__(self):
        """Super help in fetching the init method"""
        super().__init__()
        print("This is B __INIT__")
        
    def feature2(self):
        print("This is B feature")
        
class C(A,B):
    
    def __init__(self):
        super().__init__()
        print("This is C init")
        
    def feature3(self):
        print("This is B feature")

c1=C()
c1.fe
-----------------------------

So it is providing the result from left to right:
    means:
    [A]    [B]
      \     /
       \   /
        \ /
        [C]: 

Now here: Method resolution Order? (MRO)
Ans It basically start the code from left to right: So A is at left and B at right.

This is the reason why it is not providing the data of B.

Q)  Now if we have same feature in A and B?
Ans Than it will print the feature as per MRO. So it will be feature of A.
----------------------------


===========================================================
Special Chartcter
===========================================================
1) __init__ : 
    
==================================
2) __str__ : It basically help in providing all the information in a single go.
            For ex normally we have to do object.method or attributes

By just calling an object we get the all the attributes in a single go

def __str__(self):
    return"Title: %s"%(self.title)

Object is Python:

To call it we have to use: print(Python)

==================================
    
3) __len__ : To find out a length
    
    
def __len__(self):
    return self.pages

==================================
4) __del__ : we can delete just by : del Object.

def __del__(self):
    print("A book is destroyed")
    
    
    
    



===================xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx======================================

Questions:
    
Q1.For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


Ans

class Account():
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        
    def __str__(self):
        return "Account owner: {} and Account balance: {}".format(self.owner, self.balance)
    
    def deposite(self,deposite1):
        self.deposite1=deposite1        
        return self.balance+self.deposite1
        #print("depoisite accepted")
    
    def withdraw(self,withdraw1):
        self.withdraw1=withdraw1
        if self.withdraw1>self.balance:
            print("Funds Unavailable!")
        else:
            return self.balance-self.withdraw1
            #print("withdrawal accepted")
            
acct1 = Account('Jose',100)
#print(acct1)
#acct1.deposite(100)
#acct1.deposite(50)

acct1.withdraw(50)
#acct1.withdraw(500)

-------------------------------
Q2.

Create a class cylinder and make 2 method:
    1) Volume of cylinder
    2) surface area of cylinder
    
Ans
class Cylinder:
    pi=3.14
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    #v=2*pi*r**2*h    
    def volume(self):
        return (self.pi*self.radius**2*self.height)
        
    #A=2πrh+2πr2
    def surface_area(self):
        return (2*self.pi*self.radius*self.height)+(2*self.pi*self.radius**2)
    
c = Cylinder(2,3)
#c.volume()
c.surface_area()

--------------------------------    

Q3.Create a bank Machine to withdraw and deposite money.
If the withdrwal exceed the balance then show "Amount auavialable"
Functions:
    
s.deposit() 
s.withdraw() 
s.display() 


# Python program to create Bankaccount class 
# with both a deposit() and a withdraw() function 
class Bank_Account: 
	def __init__(self): 
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 

	def deposit(self): 
		amount=float(input("Enter amount to be Deposited: ")) 
		self.balance += amount 
		print("\n Amount Deposited:",amount) 

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\n You Withdrew:", amount) 
		else: 
			print("\n Insufficient balance ") 

	def display(self): 
		print("\n Net Available Balance=",self.balance) 

# Driver code 

# creating an object of class 
s = Bank_Account() 

# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 


