#import deque library for queue usage
from collections import defaultdict, deque
from typing import Sized

#Stack class and methods
class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)

#Queue class and methods
class Queue():
    def __init__(self):
        self.queue = deque()
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
    def get_size(self):
        return len(self.queue)
    def __str__(self):
        return str(self.queue)
    
#MaxHeap class and methods
class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push (self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return None
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max
    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self,index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self) -> str:
        return str(self.heap)


#Simple and Double linked lists classes and methods

#Used for linked lists
class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    def __str__(self) -> str:
        return('(' + str(self.data) + ')')

class LinkedList:
    def __init__(self,r = None):
        self.root = r
        self.size = 0
    def add(self, d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size += 1
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None
    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node =this_node.next_node
        return False
    
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')

class DoubleLinkedList:
    def __init__(self, r = None):
        self.root = r
        self.last = r
        self.size = 0
    
    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            elif this_node.next_node == None:
                return False
            else: #move along the list
                this_node = this_node.next_node
    
    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None: #delete a node in the middle of the list
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else: #delete the las node
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else: #delete root node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True 
            else:
                this_node = this_node.next_node
        return False #data not found on the list

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node, end='->')
        print()

#Trees classes and methods
class BST:
    def __init__(self, data, left=None, right= None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False #duplicated value
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = BST(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = BST(data)
                return True

    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1

    def preorder(self):
        if self is not None:
            print(self.data, end = ' ')
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()

    def posorder(self):
        if self is not None:
            if self.left is not None:
                self.left.posorder()
            if self.right is not None:
                self.right.posorder()
            print(self.data, end = ' ')
    

