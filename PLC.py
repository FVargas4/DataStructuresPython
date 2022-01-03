import random

#create list with values under 10
under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10))

#create list with squared values of the list under_10
sqr = [x**2 for x in under_10]
print('squares: '+ str(sqr))

#get odd numbers from range to 10
odds = [x for x in range(10) if x%2 == 1]
print('odds: ' + str(odds))

#get even numbers from range to 10
even = [x for x in range(10) if x%2 == 0]
print('even: ' + str(even))


#get multiples of 10
ten_x = [x * 10 for x in range (10)]
print('ten_x: ' + str(ten_x))

#get numbers from a string
string = 'I love 2 go t0 the store 7 times a w3ek.'
nums = [x for x in string if x.isnumeric()]
#.join makes a string of all elements in list
print('numbers in string: ' + ''.join(nums))

'''Alternativa para .join(list)
response = ''
for x in nums:
    response += x
print(response)'''

names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
print('index= '+str(idx[0]))

letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)

nums = [5, 3, 10, 18, 6, 7]
new_list = [x if x%2 == 0 else 10*x for x in nums]
print('new_list: '+ str(new_list))
