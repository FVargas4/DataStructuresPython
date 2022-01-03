'''Use an list as a stack
#create a stack with a list
my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)

print(my_stack)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack)'''

import DS_classes as DS

#use Stack class to create a stack
my_stack = DS.Stack()
my_stack.push(1)
my_stack.push(4)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
