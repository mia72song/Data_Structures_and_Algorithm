# Queue 隊列：FIFO 先進先出
class Queue:
    def __init__(self):
        self.__list = []
        
    def is_empty(self):
        return self.__list==[]
    
    def enqueue(self, item):
        self.__list.append(item)
    
    def dequeue(self):
        item = self.__list.pop(0)
        return item
    
    def size(self):
        return len(self.__list)

# Deque 雙端隊列 (double-ended queue)
class Deque:
    def __init__(self):
        self.__list = []
    
    def is_empty(self):
        return self.__list==[]
    
    def add_front(self, item):
        self.__list.insert(0, item)
    
    def add_rear(self, item):
        self.__list.append(item)
    
    def pop_front(self):
        item = self.__list.pop(0)
        return item
    
    def pop_rear(self):
        item = self.__list.pop(-1)
        return item
    
    def size(self):
        return len(self.__list)
    
if __name__=="__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.is_empty())
    print(q.size())
    print("============")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
