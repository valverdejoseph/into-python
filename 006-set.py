#A type of collection, with different data types and unique elements,
#but unordered: it doesn't record element position
my_set={'rock',1,True,'rock'}
my_set #{1, 'rock'}
#From list to set, set(), called Type Casting:
my_li=[0,1,'rock']
my_li #[0, 1, 'rock']
aset=set(my_li)
aset #{0, 1, 'rock'}
bset=set([1,True,False])
bset #{False, 1}
#To add an item, .add():
bset.add('grunge')
bset #{False, 1, 'grunge'}
#To remove an item, .remove():
bset.remove(False)
bset #{1, 'grunge'}
#To check if an item is in the set, in:
False in bset #False
True in bset #True
#To intersect, use '&':
inter=aset&bset&my_set
inter #{1}
#To unite, .union():
uni=aset.union(bset,inter)
uni #{0, 1, 'grunge', 'rock'}
#To check if a set is a subset, .issubset():
inter.issubset(aset) #True
aset.issubset(inter) #False
