#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:51:38 2019

@author: tianhang.chen
"""

"""
4.1问题：找出数组中唯一的重复元素。
"""

#1.哈希法：空间换时间。时间复杂度n，空间复杂度n。
def hashfind_dup(arr, n):
    if arr == None:
        return None
    hash_tool = {k : 0 for k in range(1, n+1)}
    for i in arr:
        if hash_tool[i] == 1:
            return i
        if hash_tool[i] == 0:
            hash_tool[i] = 1
        
if __name__ == '__main__':
    arr = list(range(1,1001))
    arr.append(888)
    n = 1000
    #dup = hashfind_dup(arr,n)
    

#2.累加法。时间复杂度n，空间复杂度1.
def sumfind_dup(arr, n):
    if arr == None:
        return None
    basic_sum = sum(list(range(n+1)))
    delta = sum(arr) - basic_sum
    return delta

if __name__ == '__main__':
    arr = list(range(1,1001))
    arr.append(888)
    n = 1000
    #dup = sumfind_dup(arr,n)
    
#3.异或法。时间复杂度n，空间复杂度1
def xorfind_dup(arr, n):
    if arr == None:
        return None
    m = 0
    for i in arr:
        m = m ^ i
    for j in range(1, n+1):
        m = m ^ j
    return m

if __name__ == '__main__':
    arr = list(range(1,1001))
    arr.append(888)
    n = 1000
    #dup = xorfind_dup(arr, n)
    
#4.数据映射法。时间复杂度为n，空间复杂度为0.
def mapfind_dup(arr,n):
    if arr == None:
        return None
    arr = list(arr)
    i = 0
    while True:
        if arr[i] < 0:
            return -arr[i]
        arr[i] = - arr[i]
        i = -arr[i]
        if i > len(arr):
            return None


if __name__ == '__main__':
    arr = list(range(1,1001))
    arr.append(887)
    n = 1000
    #dup = mapfind_dup(arr, n)
    
#5.单链表环形相遇法：
def lmeet_dup(arr,n):
    if arr == None:
        return None
    slow = 0
    fast = 0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
        
    fast = 0
    while True:
        fast = arr[fast]
        slow = arr[slow]
        if fast == slow:
            return slow
        git 
if __name__ == '__main__':
    arr = list(range(1,1001))
    arr.append(887)
    n = 1000
    dup = lmeet_dup(arr, n)
        
    
    
    
    
    
    
    