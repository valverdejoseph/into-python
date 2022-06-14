#With Exception Handling, errors in program execution can be caught 
#and alternative steps can be taken instead of terminating the program
#First, the program tries to execute the Try block, but if an error occurs,
#execution will pass to the exception that matches that error
try:
  file=open('my_file','r')
  file.write('My file of mine.')
except IOError:
  print('Unable to open or read the data in the file.')
except: #For errors that aren't specified. This isn't a best practice
  print('Some other error occurred!')
else: #If no errors occurs
  print('The file was written successfully.')
finally: #To continue execution regardless of the end result
  file.close()
  print('File is now closed.')
