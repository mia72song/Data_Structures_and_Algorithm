import random
alist = random.sample(range(0, 100), 9)

# Bubble Sort 冒泡排序法 Ο(n^2) 穩定
# best case:O(n)
# worst case:Ο(n^2)
def bubble_sort(aList):
    n = len(aList)
    for y in range(n-1, 0, -1):
        for x in range(y):
            if aList[x]>aList[x+1]:
                aList[x], aList[x+1] = aList[x+1], aList[x]
    return aList


# Selection Sort 選擇排序法 Ο(n^2) 不穩定
# best case:O(n^2)
# worst case:Ο(n^2)
def select_sort(aList):
    n = len(aList)
    for y in range(n-1):
        min_index=None
        for x in range(y, len(aList)):
            if min_index==None:
                min_index=y
                continue
            if aList[x]<aList[min_index]:
                min_index=x
        aList[y], aList[min_index]=aList[min_index], aList[y]
    return aList

    
# Insertion Sort 插入排序法 O(n^2) 穩定
# best case:O(n)
# worst case:Ο(n^2)
def insert_sort(aList):
    n = len(aList)
    for i in range(1, n):
        while i>0 :
            if aList[i]<aList[i-1]:            
                aList[i-1], aList[i]=aList[i], aList[i-1]
            i-=1
    return aList

    
# Shell Sort 希爾排序法 O(n log n)~O(n^2) 不穩定
# best case:O(n^1.3)
# worst case:Ο(n^2)
def shell_sort(aList):
    n = len(aList)
    gap = n//2
    while gap>0 :
        for i in range(gap, n):
            while i>0 :
                if aList[i]<aList[i-gap]:            
                    aList[i-gap], aList[i]=aList[i], aList[i-gap]
                i-=gap
        gap = gap//2
    return aList


# Quick Sort 快速排序法 O(n log n) 不穩定
# best case:O(n log n)
# worst case:Ο(n^2)
def quick_sort(aList, start_index, end_index):
    if start_index<end_index:
        mid_value = aList[start_index]
        low = start_index
        high = end_index
        while low<high :
            while low<high and mid_value<aList[high] :
                high-=1
            else:
                aList[low] = aList[high]
                aList[high] = mid_value
            
            while low<high and mid_value>aList[low] :
                low+=1
            else:
                aList[high] = aList[low]
                aList[low] = mid_value
                
        mid_index = low
        quick_sort(aList, start_index, mid_index-1)
        quick_sort(aList, mid_index+1, end_index)
    
    return aList


# Merge Sort 合併排序法 O(n log n) 穩定
# best case:O(n log n)
# worst case:Ο(n log n)
def merge_sort(aList):
    n = len(aList)
    # 拆分
    if n<=1 :
        #print(aList)
        return aList
    mid = n//2
    r_list = merge_sort(aList[:mid])
    l_list = merge_sort(aList[mid:])
    
    # 合併
    r_cur, l_cur = 0, 0
    result = []
    while r_cur<len(r_list) and l_cur<len(l_list):
        if r_list[r_cur]<l_list[l_cur]:
            result.append(r_list[r_cur])
            r_cur+=1
        else:
            result.append(l_list[l_cur])
            l_cur+=1
                  
    result+=r_list[r_cur:]
    result+=l_list[l_cur:]
    #print(result)
    return result


if __name__=="__main__":
    # alist = [56]
    print(alist, "<-Original")
    print(bubble_sort(alist), "<-Bubble Sort")
    print(select_sort(alist), "<-Selection Sort")
    print(insert_sort(alist), "<-Insertion Sort")
    print(shell_sort(alist), "<-Shell Sort")
    print(quick_sort(alist, 0, len(alist)-1), "<-Quick Sort")
    print(merge_sort(alist), "<-Merge Sort")