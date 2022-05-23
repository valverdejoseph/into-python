#Expressions: Operations that the computer performs, even between compatible types
#Python follows mathematical conventions

#Addition: x + y
#Subtraction: x - y
#Multiplication: x * y
#Division: x / y, this result in a float
#Integer Division: x // y, this result in a rounded int to the nearest integer


#Variables: Memory spaces to store values
my_var = 1
x = 1 + 2 + 3 + 4
y = x / 9
type(y) #float
#To overwrite a variable to a new value:
x = x / 60


#To print variables:
print('Hi everyone!')


#To check the Python version:
import sys
print(sys.version)
#sys is a python built-in module that contains many system-specific parameters and functions
#We must explicitly import it

#System settings about float type:
sys.float_info
#sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, 
#min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, 
#dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

#When you make a mistake,
#the error message show you where the error occurred and
#what kind of error it was
#For example:
frint("Hello, Python!")
#---------------------------------------------------------------------------
#NameError                                 Traceback (most recent call last)
#Input In [5], in <cell line: 3>()
#      1 # Print string as error message
#----> 3 frint("Hello, Python!")
#NameError: name 'frint' is not defined
