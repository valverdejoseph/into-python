#A function is a code block to reuse by callings
#It takes an input to produce an output or change
#There are many pre-existing functions to import into your code

#Python has many built-in functions:
#To return the length of a type sequence or type collection, len(type):
len([0,1,2]) #3
len('my house') #8
#To return the total sum of elements in an iterable, sum(type):
sum([3,4,5]) #12
sum(('my house','your house')) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#To sort a list or tuple, sorted(type):
sorted([0,4,2]) #[0, 2, 4]
sorted(('your house','my house')) #['my house', 'your house']
#with sort method, .sort():
var_1=[0,4,2]
var_1.sort()
var_1 #[0, 2, 4]
var_2=('my house','your house')
var_2.sort()
var_2 #AttributeError: 'tuple' object has no attribute 'sort'
#To create a function:
def nameFunction(the_input):
  pass #this continues the flow of the program, as an empty statement
nameFunction(var_1) #
nameFunction() #TypeError: nameFunction() missing 1 required positional argument: 'the_input'
print(nameFunction(var_1)) #None
def otherFunction():
  pass
otherFunction(var_1) #TypeError: otherFunction() takes 0 positional arguments but 1 was given
otherFunction() #
def add5(a):
  """
  This section is the function documentation
  and it will appears with help(add5).
  To return, press 'q'
  """
  b=a+5
  return b #This return an output
add5(4) #9
add5(True) #6
add5(False) #5
add5('a') #TypeError: can only concatenate str (not "int") to str
help(add5)
#Help on function add5 in module __main__:
#
#add5(a)
#    This section is the function documentation
#    and it will appears with help(add5).
#    To return, press 'q'
#~
def mul(a,b):
  return a*b #To return the output directly
mul(4,5) #20
mul('a',4) #'aaaa'
def py():
  print('python3 is good')
  #a function without return
py #<function py at 0x7fdba9bd3e50>
py() #python3 is good
print(py())
#python3 is good
#None
def printElements(var):
  for i,e in enumerate(var):
    print('index:',i,'element:',e)
printElements(var_2)
#index: 0 element: my house
#index: 1 element: your house
#To input a variable number of elements, *input:
def printElements2(*var):
  for e in var:
    print(e)
printElements2(var_2) #('my house', 'your house')
printElements2(var_1) #[0, 2, 4]
printElements2(['hola','lola']) #['hola', 'lola']
printElements2(1,2)
#1
#2
#Variables that are defined outside of any function
#are within the global scope, Global Variables:
#they can be accessed anywhere after they are defined
#Variables that are defined in a function are called Local Variables,
#and only exist within the scope of that function
def aFunc():
  local_var=4
print(local_var) #NameError: name 'local_var' is not defined
#Variables inside the global scope can have the same name
#as variables in the local scope with no conflict.
y=2001
def aYear():
  y=2000
  print(y)
print(y) #2001
aYear() #2000
#If a variable is not defined within a function, Python will check
#the global scope
car='4x4'
def aCar():
  print(car+' is my fav')
aCar() #4x4 is my fav
#With the keyword global, a local variable will be a global variable
#after calling the function at least once
def anotherOne():
  global other
  other='other global var'
print(other) #NameError: name 'other' is not defined
anotherOne()
print(other) #other global var
