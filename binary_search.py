# Binary Search 二分搜尋
def binary_search(aList, item): #遞迴
    #print(aList)
    n = len(aList)
    if n<=0 :
        return False
    start_index = 0
    end_index = n-1
    mid_index = (start_index+end_index)//2
    
    if aList[mid_index]==item :
        return True
    elif aList[mid_index]>item :
        return binary_search(aList[:mid_index], item)
    elif aList[mid_index]<item :
        return binary_search(aList[mid_index+1:], item)
    
    return False

def binary_search2(aList, item):
    #print(aList)
    n = len(aList)
    start_index = 0
    end_index = n-1
    while end_index>=start_index :
        mid_index = (start_index+end_index)//2
        if aList[mid_index]==item :
            return True
        elif aList[mid_index]>item :
            end_index = mid_index-1
        elif aList[mid_index]<item :
            start_index = mid_index+1
        
    return False 
    
if __name__=="__main__" :
    import random
    alist = random.sample(range(0, 20), 9) 
    
    from sort import bubble_sort
    alist = bubble_sort(alist)
    # print(alist)
    
    print(alist, "<-Sorted List")
    print(binary_search(alist, 15))
    print(binary_search2(alist, 15))