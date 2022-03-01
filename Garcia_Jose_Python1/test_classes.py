from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the user’s username, password, registration date, and more. 
Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values

ar1 = Arithmetic(7,20)
print(ar1.add())
print(ar1.divide())
print(ar1.remainder())


ar2 = Arithmetic(5,50)
print(ar2.add())
print(ar2.divide())
print(ar2.remainder())

ar3 = Arithmetic(3,60)
print(ar3.add())
print(ar3.divide())
print(ar3.remainder())

ar4 = Arithmetic(80,550)
print(ar4.add())
print(ar4.divide())
print(ar4.remainder())


## I initially misunderstood the instructions and created my own Class with its arithmetics. 
##I listed it below and commented it out for safekeeping/future practice.
'''class Arithmetic():
    #explain the purpose of this class
    explanation = "I have different arithmetics stored as methods"
    
    def explain(self):
        print(self.explanation)
        
    #define two values as integer for arithmetic    
    def __init__(self,x=1,y=1):
        self.x = x
        self.y = y
    
    #Create methods to bring each arithmetic operation
    def add(self,x,y):
        print("I added {} and {}.".format(x,y))
        return x + y
    
    def subtract(self,x,y):
        print("I subtracted {} from {}.".format(y,x))
        return x - y
    
    def divide(self,x,y):
        print("I divided {} by {}.".format(x,y))
        return x/y
    
    def remainder(self,x,y):
        print("I find the remainder between {} and {} when they are divided.".format(x,y))
        return x%y
    
    def multiplication(self,x,y):
        print("I multiplied {} and {}.".format(x,y))
        return x*y
    '''