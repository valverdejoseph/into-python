#Comparison operations produce a Boolean
#This example is for Integers, but it applies to different data types
a=4
#To check equality, ==:
a==7 #False
a==4 #True
#To check inequality, !=:
a!=7 #True
a!=4 #False
#To check greater than, >:
a>4 #False
a>3 #True
#To check greater than or equal, >=:
a>=4 #True
a>=3 #True
#To check less than, <:
a<4 #False
a<3 #False
#To check less than or equal, <=:
a<=4 #True
a<=3 #False
#To deny a boolean, not():
not(False) #True
not(a<=4) #False
#To check the truth of one boolean or another, or:
False or False or False #False
False or True #True
a<=4 or a<=3 #True
#To check the truth of one boolean and another, & (and):
False & False & True #False
True and True #True
a<=4 and a<=3 #False

#The If statement: Code execution depends on verifying
#the truth of the preceding comparison operation
your_age=12
if(your_age>=18):
  print('enter')

your_age=21
if(your_age>=18):
  print('enter') #enter

#The Else statement will execute another block of code
#if the preceding comparison operation is false
your_age=12
if(your_age>=18):
  print('enter')
else:
  print("you can't enter") #you can't enter

your_age=21
if(your_age>=18):
  print('enter')
else:
  print("you can't enter") #enter

#The Elif (else-if) statement will execute another block of code
#if the preceding comparison operation is false
#and another comparison operation is true
your_age=12
if(your_age>=18):
  print('enter')
elif(your_age>=17):
  print('you can enter with some conditions')
else:
  print("you can't enter") #you can't enter

your_age=17
if(your_age>=18):
  print('enter')
elif(your_age>=17):
  print('you can enter with some conditions')
else:
  print("you can't enter") #you can enter with some conditions

your_age=21
if(your_age>=18):
  print('enter')
elif(your_age>=17):
  print('you can enter with some conditions')
else:
  print("you can't enter") #enter
