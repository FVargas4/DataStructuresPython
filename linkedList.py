import DS_classes as DS

myList = DS.LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()

print('size = '+str(myList.size))
myList.remove(8)
myList.print_list()
print('size = '+str(myList.size))
print(myList.find(5))
myList.print_list()
print(myList.root)

