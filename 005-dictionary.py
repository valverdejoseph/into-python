#A type of collection, with, instead of indexes, keys, and values
#To create a dictionary, use curly brackets where the keys are the first elements
#each followed by a colon and the value, separated by commas
#Keys and values can be any data type
#Keys are immutable and unique

dic={"spain":"real madrid","italy":"milan","germany":"bayern munich"}
dic["germany"] #'bayern munich'
#To add a new value:
dic["netherlands"]="ajax"
dic #{'spain': 'real madrid', 'italy': 'milan', 'germany': 'bayern munich', 'netherlands': 'ajax'}
#To delete a value, del():
del(dic['italy'])
dic #{'spain': 'real madrid', 'germany': 'bayern munich', 'netherlands': 'ajax'}
#To verify if a key is in the dictionary, in:
'spain' in dic #True
'real madrid' in dic #False
#To see all keys, .keys():
dic.keys() #dict_keys(['spain', 'germany', 'netherlands'])
type(dic.keys()) #<class 'dict_keys'>
#To see all values, .values():
dic.values() #dict_values(['real madrid', 'bayern munich', 'ajax'])
type(dic.values()) #<class 'dict_values'>
