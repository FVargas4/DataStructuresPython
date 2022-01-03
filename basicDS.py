
x = 'frog'
print (x[1])

#slicing on strings to create substrings

y = 'computer'
#print from location 1 to location 5
print (y[1:5])

#print from location 1 thru location 8 with a step of 2 locations
print (y[1:8:2])

#print from the beggining to the location 5 of the string.
print (y[:5])

'''negative indexes (from right to left)'''

#print last element
print(y[-4:])


print('t' in y)

#run thru all locations of the string
for index, item in enumerate(y):
    #Check if the index is the fifth one, print the index and the content
    if index == 5:
        print(index, item)
    #in any other case, print the message
    else:
        print('Not this one')
#create an empty string called response
response = ''
#run thru the sorted (by the first letter) string 
for item in sorted(y):
    #add i sorted letter to the response string
    response += + item
print (response)


z = ('Hector', 'Gabriel', 'Sofia', 'Ivana', 'Julieta', 'Leo', 'Fer')

#create an empty string called response
res = ''
#run thru the sorted (by the second letter) tuple 
for item in sorted(z, key=lambda k: k[1]):
    #add i sorted element to the response string
    res = res + item + ' '
print (res)

#Ask which index does _____ has on the tuple
'''Do not forget to use str() for making the whole information a string, if not error will be deployed'''
print('Index: '+ str(z.index('Fer')))


#Asign each element on a list/tuple a variable MUSST BE THE SAME NUMBER!!!
a, b, c, d, e, f, g = z

print(a, b, c, d, e, f, g)

