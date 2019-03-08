#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#二叉树遍历

from binarytree import tree
my_tree = tree(height=3, is_perfect=False)
print(my_tree)
root_value = my_tree.value
root_left = my_tree.left

#1. 先序遍历（根、左、右）
def preorder(my_tree):
    print(my_tree.value)
    if my_tree.left is not None:
        preorder(my_tree.left)
    if my_tree.right is not None:
        preorder(my_tree.right)

if __name__ == "__main__":
    print("preorder")
    preorder(my_tree)


#1.2 先序遍历非递归（使用栈）
from queue import LifoQueue
def preorder_stack(my_tree):
    s = LifoQueue()
    t = my_tree
    while t is not None or not s.empty():
        while t is not None:
            print(t.value)
            s.put(t.right)
            t = t.left
        t = s.get()

if __name__ == "__main__":
    print("preorder_stack")
    preorder_stack(my_tree)
    

#2. 后序遍历（左、右、根）
def postorder(my_tree):
    if my_tree.left is not None:
        preorder(my_tree.left)
    if my_tree.right is not None:
        preorder(my_tree.right)
    print(my_tree.value)

if __name__ == "__main__":
    print("postorder")
    postorder(my_tree)
    

#3. 中序遍历（左、根、右）
def middleorder(my_tree):
    if my_tree.left is not None:
        preorder(my_tree.left)
    print(my_tree.value)
    if my_tree.right is not None:
        preorder(my_tree.right)

if __name__ == "__main__":
    print("middleorder")
    middleorder(my_tree)
    
    
#4. 广度优先遍历
from queue import Queue
q = Queue()
def breadthfirst(my_tree):
    q.put(my_tree)
    while not q.empty():
        p = q.get() 
        print(p.value)
        if p.left is not None:
            q.put(p.left)
        if p.right is not None:
            q.put(p.right)

if __name__ == "__main__":
    print("breadthfirst")
    breadthfirst(my_tree)