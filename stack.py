# Stack 堆疊 ：LIFO後進先出
class Stack:
    def __init__(self):
        self.__list = []
    
    def is_empty(self):
        return self.__list==[]
    
    def append(self, item):
        self.__list.append(item)
    
    def pop(self):
        item = self.__list.pop()
        return item
    
    def peek(self):
        return self.__list(-1)
    
    def size(self):
        return len(self.__list)
    
if __name__=="__main__":
    s = Stack()
    print(s.is_empty())
    
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)
    print(s.is_empty())
    print(s.size())
    
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())