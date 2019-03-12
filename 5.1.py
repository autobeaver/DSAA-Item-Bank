#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 00:08:12 2019

@author: tianhang.chen
"""

#5.1 找出字符串的全部排列组合

def get_all_permutation(text, target):
    
    text = list(text)
    
    if target == len(text) - 1:
        print(''.join(text))
        return
    
    for i in range(target, len(text)):
        if i == target:
            get_all_permutation(text, target+1)
        else:
            if text[target] != text[i]:
                text[target], text[i] = text[i], text[target]
                get_all_permutation(text, target+1)
                text[i], text[target] = text[target], text[i]

if __name__ == '__main__':
    text = 'aag'
    get_all_permutation(text, 0)
    

