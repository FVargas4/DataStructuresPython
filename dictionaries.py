#constructors
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
print(x)
#using tuples
x = dict([('pork', 20.0), ('beef', 30.0), ('chicken', 40.0)])
print(x)
#easiest
x = dict(pork=30.0, beef=40.0, chicken=21.1)
print(x)

'''dictionaries operations'''
#add or update element
x['shrimp'] = 50.0
print(x)
#delete an element on the dictionary
del(x['shrimp'])
print(x)
#print the # of elements on the dictionary
print(len(x))
#clear dictionary
x.clear()
print(x)


'''accessing keys and values on a dictionary'''
y = dict(pork=30.0, beef=40.0, chicken=21.1)
#print array of dictionary keys
print(y.keys())
#print array of dictionary values
print(y.values())
#print array of dictionary key-value pairs
print(y.items())

#check membership in y_keys (ONLY KEYS)
print('beef' in y)

#check membership in y_values (ONLY VALUES, NOT KEYS)
print('beef' in y.values())

#iterating on a dictionary
for key in y:
    print(key, y[key], '\n')

for k, v in y.items():
    print(k,v)

