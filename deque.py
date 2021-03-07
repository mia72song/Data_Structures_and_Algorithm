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
    d = Deque()
    print(d.is_empty())
    d.add_front(1)
    d.add_front(2)
    d.add_rear(3)
    d.add_rear(4)
    print(d.is_empty())
    print(d.size())
    print(d.pop_front())
    print(d.pop_rear())
    print(d.pop_front())
    print(d.pop_rear())