import DS_classes as DS

dll = DS.DoubleLinkedList()
for i in [1,2,3,4,5,3]:
    dll.add(i)

print('size = '+str(dll.size))
dll.print_list()
dll.remove(3)
print('size = '+str(dll.size))

print(dll.remove(15))
print(dll.find(15))
dll.add(21)
dll.add(22)
dll.remove(5)
dll.print_list()
print(dll.last.prev_node)