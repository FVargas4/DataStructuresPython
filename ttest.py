import DS_classes as DS

tree = DS.BST(7)
tree.insert(9)

for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
    tree.insert(i)

for i in range(16):
    print(tree.find(i), end=' ')
print('\n', tree.get_size())

print(tree.preorder())
print(tree.inorder())
print(tree.posorder())