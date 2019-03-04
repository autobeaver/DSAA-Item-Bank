#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:46:51 2019

@author: tianhang.chen
"""

#1.3
def sum_l(head):
    temp = head.next
    m = 1
    answer = 0
    while temp is not None:
        answer = answer + m * temp.date
        m *= 10
        temp = temp.next
    return answer

answer = sum_l(head1) + sum_l(head2)
        