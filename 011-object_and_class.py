#Each of the different data types or classes is an object
#Also, an object is an instance of a particular data type
a=1 #is an object, and an instance of int
b=False #is an object, and an instance of bool
#To get the type of an object, type():
type(a) #<class 'int'>
type(b) #<class 'bool'>
#An object is made up of: a type name, internal representation,
#and methods, which are proper functions
#To return the number of bits necessary to represent self in binary, .bit_length():
a.bit_length() #1
#Knowing how to use the methods is often enough rather than
#knowing how they are implemented
#To create a class:
#A class is made up of: data attributes, and methods
class Book(object): #Class definition, Name, and Parent of the class
  #Now, the data attributes that define the objects or instances of the class
  #To initialize each instance:
  def __init__(self,title=None,pages=0):
    #__init__ is a method or constructor
    #(there are other special functions to make more complex classes),
    #self parameter refers to the newly created instance, and
    #title and pages are parameters of the newly created instance
    self.title=title
    self.pages=pages
#To create an instance:
aBook=Book('The Lord of the Rings',1200)
bBook=Book('The Bible',10000)
