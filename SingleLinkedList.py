#單向鏈表 Single Linked List
class Node:
    def __init__(self, value):
        self.dataValue = value
        self.nextValue = None
        
class SingleLinkedList:
    def __init__(self, node=None):
        self.__headValue = node
    
    def is_empty(self):
        return self.__headValue is None
    
    def print_list(self):
        cursor = self.__headValue
        print("[", end="")
        while cursor is not None:
            if cursor is self.__headValue:
                print(cursor.dataValue, end="")
            else:
                print(",", cursor.dataValue, end="")
            cursor = cursor.nextValue
        print("]")
    
    def length(self):
        if self.is_empty():
            return 0
        else:
            cursor = self.__headValue
            count = 1
            while cursor.nextValue is not None:
                cursor = cursor.nextValue
                count+=1
            return count
    
    def append(self, newValue): #由尾部添加
        node = Node(newValue)
        if self.is_empty():
            self.__headValue = node
        else:
            cursor = self.__headValue
            while cursor.nextValue is not None:
                cursor = cursor.nextValue
            cursor.nextValue = node
    
    def shift(self, newValue): #由頭部添加
        node = Node(newValue)
        if self.is_empty():
            self.__headValue = node
        else:
            node.nextValue = self.__headValue
            self.__headValue = node
            
    def insert(self, index, newValue): #指定位置(index)插入
        if index<=0 :
            self.shift(newValue)
        elif index>(self.length()-1):
            self.append(newValue)
        else:
            node = Node(newValue)
            pre_cursor = self.__headValue
            cursor = self.__headValue.nextValue            
            count = 1
            while cursor.nextValue is not None:
                if count==index:
                    pre_cursor.nextValue = node
                    node.nextValue = cursor
                    break
                else:
                    pre_cursor = cursor
                    cursor = cursor.nextValue
                    count+=1
                       
    def search(self, targetValue):
        if self.is_empty():
            return False
        else:
            cursor = self.__headValue
            while cursor is not None:
                if cursor.dataValue==targetValue:
                    return True
                cursor = cursor.nextValue
            return False
        
    def remove(self, targetValue):
        pre_cursor = None
        cursor = self.__headValue
        while cursor is not None:
            #print("當前cursor=", cursor.dataValue)
            #print(cursor.dataValue==targetValue)
            if cursor.dataValue==targetValue:
                #情況一：如果要刪除的是頭節點
                #情況三：如果要刪除的是唯一的節點
                if cursor is self.__headValue:
                    self.__headValue = cursor.nextValue
                else:
                    #正常情況
                    #情況二：如果要刪除的是尾節點
                    pre_cursor.nextValue = cursor.nextValue
                break
            else:
                pre_cursor = cursor
                cursor = cursor.nextValue
        else:
            raise ValueError(f"list.remove({targetValue}): {targetValue} not in list")
        
if __name__=="__main__":
    n1 = Node(2)
    sll = SingleLinkedList(n1)
    #print(sll.is_empty())
    sll.append(1)
    sll.shift(3)
    sll.print_list()
    #print(sll.length())
    sll.insert(1, 4)
    sll.print_list()
    #print(sll.length())
    sll.insert(-1, 5)
    sll.insert(11, 5)
    sll.print_list()
    #print(sll.search(0))
    #print(sll.search(1))
    sll.remove(0)
    sll.remove(5)
    sll.remove(5)
    sll.print_list()
    print(sll.search(5))