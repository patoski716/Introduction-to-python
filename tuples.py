# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create Tuples
fruits = ('Apples','Oranges','Pawpaw')

#Contructor
fruits2 = tuple(('Apples','Oranges','Pawpaw'))

#Single value 
fruito = ('Apple',)

print(fruits)
print(type(fruits))
print(fruits2)
print(fruito)

print(fruits2[0])

#get length
print(len(fruits))
del fruito

fruits[1]='Pear'
print(fruits)


# A Set is a collection which is unordered and unindexed. No duplicate members.

rice={'ofada','jollof','stew','fried','concosion'}
print(type(rice))
print(rice[1])
