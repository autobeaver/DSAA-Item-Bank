#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this is a cluster of sort method for arr, the description of arr is as follows.
and test with python list.  
"""


arr = [1,4,7,2,3]

#1. insert sort (local algrithm)
#from head
def insert_sort(arr):
    
    for i in range(len(arr)-1):
        j = i 
        target = arr[j+1]
        while j > 0 and target < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = target
    return arr

if __name__ == '__main__':
    arr_sort = insert_sort(arr)

#2. select sort(local algrithm)
def select_sort(arr):
    
    target = None
    for i in range(len(arr)):
        target = arr[i]
        j = i + 1
        while j <= len(arr) - 1:
            if target >= arr[j]:
                m = arr[j]
                arr[j] = target
                target = m
            j += 1
    return arr

if __name__ == '__main__':
    arr_sort2 = select_sort(arr)
        
#3.exchange sort
def exchange_sort(arr):
    for i in range(len(arr) - 1):
        count = 0
        for j in range(i,len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        if count == 0:
            return arr

if __name__ == '__main__':
    arr_sort3 = exchange_sort(arr)            

#4.merge sort 
def merge(left,right):
    result =[]
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1 
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    num = len(arr) // 2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left, right)

if __name__ == '__main__':
    arr_sort4 = merge_sort(arr)    

#5.quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    divide = arr[0]
    left = []
    right = []
    for i in arr:
        if i <= divide:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + quick_sort(right)

if __name__ == '__main__':
    arr_sort5 = quick_sort(arr)  










       