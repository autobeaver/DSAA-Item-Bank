#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:33:18 2019

@author: tianhang.chen
"""

#6.1判断一个自然数是否是某个数的平方和
#1直接法
def sqrt_search(m):
    for i in range(m):
        if i ** 2 == m:
            return i
    return None

if __name__ == "__main__":
    answer1 = sqrt_search(23)
    answer2 = sqrt_search(16)
    
#2利用2分法
def sqrt_search_bin(m):
    low = 1
    high = m
    while low < high:
        middle = (low + high) // 2
        if middle ** 2 == m:
            return middle
        elif middle ** 2 < m:
            low = middle + 1
        else:
            high = middle - 1
    return None
    

if __name__ == "__main__":
    answer3 = sqrt_search_bin(23)
    answer4 = sqrt_search_bin(16)