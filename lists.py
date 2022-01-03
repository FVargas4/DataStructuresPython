#Create empty list
x = list()

#Create multiple value list
y = ['a', 25, 'dog', 8.43]
#make a list out of a tuple
tuple1 = (10,20)
z = list(tuple1)

print(y)
print(z)

#Create a list of elements in the range [0-8)
a = [m for m in range(8)]
print(a)

#Create a list of squared elements in the range [0-10) if the value is grater than 4
b = [i**2 for i in range(10) if i>4]
print(b)

#delete value x of the list
del(y[1])
print(y)

'''Can delete a whole list with the same function del(x)'''
#add element to the tail of the list (can be used in lists)
y.extend(a)
print (y)

#add elemento to an specific index on the list (can be used in lists)
z.insert(1,b)
print(z)

#pop function (used in queues and stack) deletes the last element of the array
'''This function returns the element that has been poped out'''
print(z.pop())


#remove function removes the first corresponding elemento on the list
ex = [1, 2, 3, 4, 5, 3]
print(ex)
ex.remove(3)
print(ex)

#reverse the original list
ex.reverse()
print(ex)

#inplace sort
ex.sort()
print(ex)
'''Sorted() function returns a new list of the sorted elements of the list
Example:
newEx = sorted(ex)
print(newEx)
'''
#inplace reverse sort (descending order)

ex.sort(reverse=True)
print(ex)