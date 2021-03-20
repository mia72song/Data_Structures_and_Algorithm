# Binary Tree 二元樹
class Node:
    def __init__(self, dataValue):
        #每一個節點(Node) 最多只能擁有 2 個子節點
        self.data = dataValue
        self.l_child = None
        self.r_child = None

        
class BinaryTree:  # 傾向完整二元樹 Complete Binary Tree   
    def __init__(self):
        self.root = None
    
    def add(self, data):  # 廣度(層次)優先添加：由上而下，由左至右
        node = Node(data)
        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)
            if currentNode is None :
                self.root = node
                break
            
            if currentNode.l_child is None:
                currentNode.l_child = node
                break
            else:
                queue.append(currentNode.l_child)
            
            if currentNode.r_child is None:
                currentNode.r_child = node
                break
            else:
                queue.append(currentNode.r_child)
    
    def breadth_travel(self):  # 廣度(層次)優先遍歷
        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)
            print(currentNode.data, end=" ")
            if currentNode is None:
                break
            
            if currentNode.l_child is not None:
                queue.append(currentNode.l_child)
                
            if currentNode.r_child is not None:
                queue.append(currentNode.r_child)
                
    '''深度優先遍歷：
    PreOrder 先序(root最先)：【root】 -> Left Sub-tree -> Right Sub-tree
    PostOrder 後序(root最後)：Left Sub-tree -> Right Sub-tree -> 【root】
    InOrder 中序(root置中)：Left Sub-tree -> 【root】 -> Right Sub-tree
    '''
    def preOrder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preOrder(node.l_child)
            self.preOrder(node.r_child)
            
    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.l_child)
            print(node.data, end=" ")            
            self.inOrder(node.r_child)
    
    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.l_child)
            self.postOrder(node.r_child)
            print(node.data, end=" ")
                     
if __name__=="__main__":
    tree = BinaryTree()
    tree.add(0) #root
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.breadth_travel()
    print(" ")
    tree.preOrder(tree.root)
    print(" ")
    tree.inOrder(tree.root)
    print(" ")
    tree.postOrder(tree.root)
    print(" ")