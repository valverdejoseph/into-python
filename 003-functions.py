#print() is a function. You passed the string 'Hello, Python!' as an argument to instruct Python on what to print.
print('Hi everyone!')

# Check the Python Version
#sys is a built-in module that contains many system-specific parameters and functions,
#including the Python version in use. Before using it, we must explictly import it.
import sys
print(sys.version)

# Print string as error message
frint("Hello, Python!")
#---------------------------------------------------------------------------
#NameError                                 Traceback (most recent call last)
#Input In [5], in <cell line: 3>()
#      1 # Print string as error message
#----> 3 frint("Hello, Python!")
#NameError: name 'frint' is not defined
#The error message tells you:
#  1. where the error occurred (more useful in large notebook cells or scripts), and
#  2. what kind of error it was (NameError)

# System settings about float type
sys.float_info
#sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, 
#min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, 
#dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

#Note that strings can be represented with single quotes ('1.2') or double quotes ("1.2"), but you can't mix both (e.g., "1.2')

#Expressions in Python can include operations among compatible types

#If we save a value to an existing variable, the new value will overwrite the previous value:
# Overwrite variable with new value
x = x / 60
x
