name="Juan Carlos Holgazán"
name #'Juan Carlos Holgazán'
#To get the length:
len(name) #20
#A string as an array of words,
#each elements can be accessed using an index (in this case, 0 ~ 19)
name[0] #'J'
name[11] #' '
#With negative indexing,
#the index of the last element is -1:
name[-1] #'n'
name[-11] #'o'

#The string as a sequence performs sequence operations:
name[0:8] #'Juan Car'
#The inputs (0,8) are the start and stop indexes without including the stop
name[8:20] #'los Holgazán'
#(stride):
name[::2] #Ja alsHlaá'
#The third input (2) is the step
#(slicing):
name[0:100:2] #Ja alsHlaá'

#To concatenate a string to another variable:
fullName=name+' Orbegozo'
fullName #'Juan Carlos Holgazán Orbegozo'

#To replicate:
fullName*3
#'Juan Carlos Holgazán OrbegozoJuan Carlos Holgazán OrbegozoJuan Carlos Holgazán Orbegozo'

#To add Escape Sequences, you must add backslash (\) at the beginning,
#Escape sequences are symbols that are difficult to input
#\n, to add a new line:
print("Hey, Ronaldo\nHow are you doing?")
#Hey, Ronaldo
#How are you doing?
#\t, to add a tab:
print("Hey, Ronaldo\tHow are you doing?")
#Hey, Ronaldo   How are you doing?
#\\, to add a backslash, or place an 'r' in front of the string:
print("Hey, Ronaldo\\How are you doing?")
#Hey, Ronaldo\How are you doing?
print(r"Hey, Ronaldo\How are you doing?")
#Hey, Ronaldo\How are you doing?

#Methods,
#are special functions associated with the objective data
#upper()
name.upper() #'JUAN CARLOS HOLGAZÁN'
#replace()
name.replace('Carlos','araña') #'Juan araña Holgazán'
#find(), the result is the first index you are looking for, otherwise, -1
name.find('aña') #-1
name.find('Juan') #0
