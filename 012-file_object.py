#File objects are used to get data from files
#To open a file, open():
#the arguments are the file path and the mode: r - reading, w - writing,
#a - appending, r+ - reading and writing (cannot truncate the file.),
#w+ - writing and reading (truncates the file), and
#a+ - appending and reading (creates a new file if none exists)
file_1=open("Documents\example.txt","r")
type(file_1) #<class '_io.TextIOWrapper'>
#To get the name, .name:
file_1.name #'Documents\\example.txt'
#To see the mode that it was opened, .mode:
file_1.mode #'r'
#To see if the file is open, .closed:
file_1.closed #False
#To close the file object, .close():
#this frees up computing resources
file_1.close()
file_1.closed #True
#It is a better practice to open a file with the 'with' keyword,
#because this will automatically close the file
with open("Documents\example.txt","r") as file_1:
  #To read the file as a string, .read():
  #this method can receive an integer as number of characters
  #(.read(int)) and it will read the next characters if it runs again
  data=file_1.read()
  type(data) #<class 'str'>
  print(data)
  #To read the file as a list, .readlines():
  data=file_1.readlines()
  type(data) #<class 'list'>
  print(data)
  #To read a number of characters, .readlines(int):
  data=file_1.readlines(8)
  type(data) #<class 'list'>
  print(data)
  #Execute another one to read the next characters, .readlines(int):
  data=file_1.readlines(10)
  print(data)
  #To read the first line, .readline():
  data=file_1.readline()
  print(data)
  #Execute another one to read the next line, .readline():
  data=file_1.readline()
  print(data)
  #And to read characters in one line at most, .readline(int):
  data=file_1.readline(11)
  print(data)
  #Use a for to interact with each line:
  for line in file_1:
    print(line)
  
print(file_1.closed)
print(data)

#To open a file to write to it:
#if the file exists, it will be overwritten
with open("Documents\example_w.txt","w") as file_2:
  #To write to a file, .write():
  file_2.write("This is line 1\n")
  file_2.write("This is line 2\n")
  
#To open a file and append data:
with open("Documents\example_w.txt","a") as file_2:
  #To write to the end of the file, .write():
  file_2.write("This is line 3\n")
  file_2.write("This is line 4\n")
  
#With block can be nested

file_1=open("Documents\example.txt","a+")
#Modes with '+' should be handled with care due to the file cursor
#To return the current position of the file in bytes, .tell():
file_1.tell() #21
#To change the position in bytes from a specific position, .seek():
#this needs two arguments: the new position, the relative position (0 -
#beginning, 1 - current position, and 2 - end)
file_1.seek(0,1)
#this moves 0 bytes from the current position
#The difference between w+ and r+ is that w+ overwrites the file
#In r+, use .truncate() to remove everything othen than the actual data
file_1.truncate()
