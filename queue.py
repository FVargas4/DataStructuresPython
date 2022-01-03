#import DS tools
import DS_classes as DS

my_queue = DS.Queue()
my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(200)
my_queue.enqueue(50)
print(my_queue)
print(my_queue.dequeue())
print(my_queue)
print('Total elements in queue: '+ str(my_queue.get_size()))