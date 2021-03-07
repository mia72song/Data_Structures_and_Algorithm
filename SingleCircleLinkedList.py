#單向循環鏈表 Single Circle Linked List
class Node:
    def __init__(self, value):
        self.dataValue = value
        self.nextValue = None
        
class SingleCircleLinkedList:
    def __init__(self, node=None):
        self.__headValue = node
        if node:
            node.nextValue = node
    
    def is_empty(self):
        return self.__headValue is None
    
    def print_list(self):
        print("[", end="")
        if self.is_empty():
            print("", end="")
        else:
            cursor = self.__headValue
            while True:
                if cursor is self.__headValue:
                    print(cursor.dataValue, end="")
                else:
                    print(",", cursor.dataValue, end="")
                
                cursor = cursor.nextValue
                if cursor is self.__headValue:
                    break
        print("]")
    
    def length(self):
        if self.is_empty():
                return 0
        else:
            cursor = self.__headValue
            count = 1
            while cursor.nextValue!=self.__headValue:
                cursor = cursor.nextValue
                count+=1
            return count
    
    def append(self, newValue): #由尾部添加
        node = Node(newValue)
        if self.is_empty():
            self.__headValue = node
            node.nextValue = node
        else:
            cursor = self.__headValue
            while cursor.nextValue!=self.__headValue:
                cursor = cursor.nextValue
            cursor.nextValue = node
            node.nextValue = self.__headValue
    
    def shift(self, newValue): #由頭部添加
        node = Node(newValue)
        if self.is_empty():
            self.__headValue = node
            node.nextValue = node
        else:
            cursor = self.__headValue
            while cursor.nextValue!=self.__headValue:
                cursor = cursor.nextValue            
            cursor.nextValue = node
            node.nextValue = self.__headValue
            self.__headValue = node
            
    def insert(self, index, newValue): # 和單鏈表完全一樣
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
        cursor = self.__headValue
        while cursor is not None:
            if cursor.dataValue==targetValue:
                return True
            cursor = cursor.nextValue
            if cursor is self.__headValue:
                break        
        return False
    
    def remove(self, targetValue):
        if self.is_empty():
            raise ValueError(f"list.remove({targetValue}): {targetValue} not in list")
        else:
            pre_cursor = None
            cursor = self.__headValue
            nex_cursor = cursor.nextValue
            #情況三：如果要刪除的是唯一的節點
            while nex_cursor is not cursor: 
                pre_cursor = cursor
                cursor = nex_cursor
                nex_cursor = nex_cursor.nextValue
                #print("當前cursor=", cursor.dataValue)
                #print(cursor.dataValue==targetValue)
                #print("當前nex_cursor=", nex_cursor.dataValue)
                if cursor.dataValue==targetValue:
                    #正常情況
                    #情況二：如果要刪除的是尾節點 成立
                    pre_cursor.nextValue = nex_cursor
                    #情況一：如果要刪除的是頭節點，再多一步驟
                    if cursor is self.__headValue:
                        self.__headValue = nex_cursor                    
                    break                
                #否則cursor巡迴一圈後，都找不到的話
                if cursor is self.__headValue:
                    raise ValueError(f"list.remove({targetValue}): {targetValue} not in list")
            else:
                #print("當前cursor=", cursor.dataValue)
                #print(cursor.dataValue==targetValue)
                if cursor.dataValue==targetValue:
                    self.__headValue = None
                else:
                    raise ValueError(f"list.remove({targetValue}): {targetValue} not in list")
   
if __name__=="__main__":
    n1 = Node(1)
    scll = SingleCircleLinkedList(n1)
    scll.remove(1)
    scll.print_list()
    #print(scll.is_empty())
    #print(scll2.is_empty())
    scll.append(2)
    scll.append(3)
    scll.append(4)
    scll.print_list()
    scll.shift(5)
    scll.shift(6)
    scll.print_list()
    #print(scll.length())
    scll.insert(2, 0)
    scll.insert(-2, 8)
    scll.insert(12, 9)
    scll.print_list()
    #print(scll.length())
    print(scll.search(8))
    print(scll.search(9))

    scll.remove(9)
    scll.print_list()
    scll.remove(8)
    scll.print_list()
    scll.remove(0)
    scll.print_list()
