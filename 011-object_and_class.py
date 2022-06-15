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
  #Next, the definition of methods, which are functions to interact and
  #change the data attributes, changing or using these
  #To know how many pages are left to read:
  def remainPages(self,pagesRead=0):
    return self.pages - pagesRead
  #To get the title length:
  def titleLen(self):
    return len(self.title)
  #To capitalize the title:
  def upTitle(self):
    self.title=self.title.upper()
#To create an instance:
#Name of object=Name of class(Attributes)
aBook=Book('The Lord of the Rings',1200) 
bBook=Book('The Bible',10000)
#To get a data attribute, .dataAttribute:
aBook.title #'The Lord of the Rings'
bBook.pages #10000
#To change a data attribute, .dataAttribute:
aBook.title='Oedipus Rex'
aBook.title #'Oedipus Rex'
#To test the methods:
aBook.remainPages(500) #700
aBook.titleLen() #21
aBook.upTitle()
aBook.title #'OEDIPUS REX'
bBook.remainPages(10) #9990
bBook.titleLen() #9
bBook.upTitle()
bBook.title #'THE BIBLE'
#To get the list of data attributes and methods of a class, dir():
dir(aBook)
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
#'__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
#'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#'__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#'__weakref__', 'pages', 'remainPages', 'title', 'titleLen', 'upTitle']
dir(int)
#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
#'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
#'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
#'__getnewargs__', '__gt__', '__hash__', '__index__', '__init__',
#'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__',
#'__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
#'__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__',
#'__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
#'__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__',
#'__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
#'__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
#'__subclasshook__', '__truediv__', '__trunc__', '__xor__',
#'as_integer_ratio', 'bit_length', 'conjugate', 'denominator',
#'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
#The attributes with underscores are for internal use, the others are
#to be taken into account
