'''TUPLES ARE UNMUTABLE AND CANNOT BE CHANGED ONCE CREATED'''
#Constructors
x = ()
x = (1, 2, 3)
x = 1, 2, 3
x = 2,

print(x, type(x))

list1 = {2, 3, 4}
x = tuple(list1)
print(x, type(x))

'''tuples' items can be changed'''

y = ([1,2,3], 4)
#delete the second position of the list in the first position of the tuple
del(y[0][1])

print(y)

y += x

print(y)

print('\n End of tuples \n Sets starts\n')

'''------SETS-----'''
#constructors

x = {3, 4, 5, 6, 7, 3}
#python ignores sets' duplicate values
print(x)

y =  set()
print (y)

z = set(list1)
print(z)

#Operations possible with sets

#add and remove
z.add(7)
print(z)
z.remove(3)
print(z)

#get length
print(len(z))

#check membership (RETURNS BOOLEAN)
print(5 in x)

#pop random item on the set
print(z.pop(), z)


#delete all items on set
z.clear()
#returns empty set
print(z)


'''Mathematical set operations'''
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 3}

#and (INTERSECTION) function
print(s1 & s2)
#or (UNION) function
print(s1 | s2)
#xor (symetric difference) function
print(s1 ^ s2)
#difference between s1 and s2 function
print(s1 - s2)
#check subset
print(s1 <= s2)
#check superset
print(s1 >= s2)




