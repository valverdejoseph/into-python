#These are compound data types, and ordered sequences of different objects

#Tuple: an inmutable sequence written with commas and parentheses
my_tup=(10,'tuple',0,-1.4,True)
type(my_tup) #<class 'tuple'>
my_tup[0] #10
my_tup[-1] #True
len(my_tup) #5
#To concatenate, add '+':
my_new_tup=my_tup+(False,'square',-3.14)
my_new_tup #(10, 'tuple', 0, -1.4, True, False, 'square', -3.14)
#To return multiple elements, use slicing:
my_tup[0:3] #(10, 'tuple', 0)
#If a new tuple is defined with a created tuple,
#both reference the same elements, but without the
#possibility of changing any
tup=my_tup
tup[0]=1 #TypeError: 'tuple' object does not support item assigment
#To sort with same data types, sorted():
tup=('a','vaca','arm')
my_tup_sorted=sorted(tup) #['a', 'arm', 'vaca']
#A tuple can contain other tuples, nesting (in general):
tup_remix=(tup,my_tup,-1.1)
tup_remix #(('a', 'vaca', 'arm'), (10, 'tuple', 0, -1.4, True), -1.1)
tup_remix[0] #('a', 'vaca', 'arm')
tup_remix[0][1] #'vaca'
#To find the first index of an existing element, .index():
tup.index('a') #0
#Otherwise, ValueError

#List: a mutable sequence written with commas and square brackets
my_list=['hola',9,4]
type(my_list) #<class 'list'>
#This also nest other data structures
my_new_list=[my_list,tup,True]
my_new_list #[['hola', 9, 4], ('a', 'vaca', 'arm'), True]
#Slicing is also allowed:
my_new_list[1:2] #[('a', 'vaca', 'arm')]
#Note that slicing return the elements in the same data type
#To concatenate, add '+':
my_renew_list=my_list+[0]
my_renew_list #['hola', 9, 4, 0]
#To add new elements, .extend([]):
my_list.extend([1.8, 'hace'])
my_list #['hola', 9, 4, 1.8, 'hace']
#To add one element, .append():
my_list.append(False)
my_list.append([1,2,3])
my_list #['hola', 9, 4, 1.8, 'hace', False, [1, 2, 3]]
#To modify one element, use indexing:
my_list[1]=20
my_list #['hola', 20, 4, 1.8, 'hace', False, [1, 2, 3]]
#To delete an element, del():
del(my_list[4])
my_list #['hola', 20, 4, 1.8, False, [1, 2, 3]]
#To convert a string to a list, .split():
#without an argument, the separation is by a space
'hola, ¿qué haces?'.split() #['hola,', '¿qué', 'haces?']
'1, 2, 3, 4'.split(',') #['1', ' 2', ' 3', ' 4']
#To count an item, .count():
my_list.count('hola') #1
my_list.count(1) #0
#If a new list is defined with a created list,
#both reference the same elements, also called Aliasing,
#with the possibility of changing elements
other_list=my_list
other_list[4]=True
my_list #['hola', 20, 4, 1.8, True, [1, 2, 3]]
#To clone a list, [:]:
#Both lists are independent
your_list=my_list[:]
your_list[4]='Undefined'
my_list #['hola', 20, 4, 1.8, True, [1, 2, 3]]
your_list #['hola', 20, 4, 1.8, 'Undefined', [1, 2, 3]]

#To get more info on data structure, use help():
help(your_list) #to more help, press 'h'. to exit, press 'q'

#To add items from a line:
members=['Member  Date  Active  \n', '19532      2020-9-10    yes\n', '34202      2018-2-11    no\n', '45397      2020-8-7     yes\n', '12545      2016-7-17    yes\n', '11599      2016-11-24   yes\n', '17791      2016-2-20    yes\n', '30200      2020-4-10    yes\n', '29023      2017-6-19    yes\n', '95126      2020-4-2     no\n', '80321      2019-10-4    yes\n', '64116      2018-10-9    no\n', '78268      2015-4-23    no\n']
inac = [mem for mem in members if ('no' in mem)]
#equal to:
#for mem in members:
#  if 'no' in mem:
#    inactive.append(mem)
