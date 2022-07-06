#Range function outputs an ordered list:
#it starts at the first input and iterates up 
#without including the second input
range(4) #range(0, 4)
range(10,18) #range(10, 18)

#For loop: code execution will repeat statements in the indent
#for a set number of times
for i in range(4):
  print('x')
#x
#x
#x
#x
teams=['real','barce','milan','inter']
for i in range(2):
  teams[i]='win'
#
teams #['win', 'win', 'milan', 'inter']
#To iterate through a list or tuple:
for team in teams:
  print('result or future match:',team)
#result or future match: win
#result or future match: win
#result or future match: milan
#result or future match: inter
#Enumerate obtains the index and the item in the data collection:
for i,team in enumerate(teams):
  i+=1
  print('match and (result or team):',i,team)
#match and (result or team): 1 win
#match and (result or team): 2 win
#match and (result or team): 3 milan
#match and (result or team): 4 inter

#While loop: similar to for loops but instead of a set number of times,
#it runs if a condition is True
i=0
while (teams[i]=='win' or teams[i]=='lose'):
  print(i+1,'match result:',teams[i])
  i+=1
#1 match result: win
#2 match result: win
teams_size=len(teams)
while (i<teams_size and teams[i]!='win' and teams[i]!='lose'):
  print(i+1,'match team:',teams[i])
  i+=1
#3 match team: milan
#4 match team: inter
#The KeepGoing Loop:
keepgoing=True
temp=4
while keepgoing:
  print('This is the KeepGoing loop.')
  if temp<=0:
    print('This is the last output.')
    keepgoing=False
  temp-=1
#This is the KeepGoing loop.
#This is the KeepGoing loop.
#This is the KeepGoing loop.
#This is the KeepGoing loop.
#This is the KeepGoing loop.
#This is the last output.
