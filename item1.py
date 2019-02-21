#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:47:11 2019

@author: tianhang.chen
"""
#3.1
#将有序整数数组放到二叉树中
class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def array_to_tree(array,start,end):
    """transfer array to binary tree"""
    root = None
    if start <= end:
        root = BiTNode()
        mid = (start + end + 1) / 2
        root.data = array[mid]
        root.lchild = array_to_tree(array,start,mid-1)
        root.rchild = array_to_tree(array,mid+1,end)
    else:
        root = None
#用中序遍历打印该二叉树节点内容
def tree_print(root):
    if root == None:
        return
    if root.lchild != None:
        tree_print(root.lchild)
    print(root.data)
    if root.rchild != None:

        
#1.1       
#链表逆序（就地逆序）
class  LNode:
    def __new__(self,x):
        self.data = x
        self.next = None

def reverse_lsequence(head):
    #判断列表是否为空
    if head == None or head.next == None:
        return
    #创建前驱、当下、后驱指针
    pre = None
    nex = None
    cur = None
    #处理头结点
    cur = head.next
    nex = cur.next
    cur.next = None
    pre = cur
    cur = nex
    #遍历处理中间节点
    while cur.nex != None:
        nex = cur.nex
        cur.next = pre
        pre = cur
        cur = nex
    #处理尾节点
    cur.next = pre
    head.next = cur
    
def recursive_reverse(head):
    if head is None or head.next is None:
        return head
    firstnode = head.next
    newhead = recursive_reverse(firstnode)
    head.next = newhead
    return newhead


#1.2
class LNode:
    def __new__(self,x):
        self.data = x
        self.next = None

def deduplicate(head):
    if head.next == None or head == None:
        return 
    outer = head.next
    inner = None
    inner_pre = None
    while outer is not None:
        inner = outer.next
        inner_pre = outer
        while inner is not None:
            if inner.data == outer.data:
                inner_pre.next = inner.next
                inner = inner.next
            else:
                inner_pre = inner
                inner = inner.next
        outer = outer.next
        
def recursive_deduplicate(head):
    if head.next == None or head == None:
        return
    cur = head
    head_pre = cur
    head2 = cur.next
    while head2 != None:
        if cur.data == head2.data:
            head_pre = head2.next
            head2 = head2.next
        else:
            head_pre = head2
            head2 = head2.next
    cur.next = recursive_deduplicate(cur.next)
            
            
#3.3 traversal binary tree
class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None
        
        
def traversal_btree(root):
    print(root)
    return traversal_btree(root.lchild), traversal_btree(root.rchild)

            
#3.4 find max sum child tree
class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None
           
def max_subtreesum(head, allsum=0, maxsum=0):
    if head.lchild != None:
        yield find_stree(head.lchild, allsum, maxsum)
    if head.rchild != None
        yield find_stree(head.rchild, allsum, maxsum)
    allsum += head.data 
    if maxsum < allsum:
        maxsum = allsum
    if head.lchild == None and head.rchild == None:
        return maxsum
