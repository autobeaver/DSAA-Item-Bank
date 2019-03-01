#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:24:22 2019

@author: tianhang.chen
"""

"""
1.6找出单链表中是否有环
"""
#1.hash法

#2.快慢指针法
class LNode:
    def __init__(self,x):
        x.data = x
        x.next = None

def find_circle(head):
    if head == None or head.next == None:
        return None
    fast = head.next
    slow = head.next
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return fast
    return None

def find_entrance(head,meet):
    while True:
        if head == meet:
            return meet
        head = head.next
        meet = meet.next