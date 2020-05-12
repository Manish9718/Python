# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:49:07 2020

@author: HP
"""
'''Process of Tree Traversal:
    1) Declare the commen thing: rootdata, leftchild, rightchild.
    2) provide value to Nodes
    3) use 3 Traversal formula to get the value.'''

class Node:
    def __init__(self,value):
        self.leftchild = None
        self.rightchild = None
        self.rootdata = value
#create instance for node value
        
'''Here we have fixed the value of the Nodes'''
root = Node(1)
root.leftchild = Node(2)
root.rightchild = Node(3)
root.leftchild.leftchild = Node(4)
root.leftchild.rightchild = Node(5)

'''Inorder means we are ordering the root(1) or rootdata(1) inbetween the Nodes'''
def Inorder(root):
    if root:
        Inorder(root.leftchild)
        print(root.rootdata)
        Inorder(root.rightchild)
Inorder(root)

'''Here we are calling the root in the starting'''
def Preorder(root):
    if root:
        print(root.rootdata)
        Preorder(root.leftchild)
        Preorder(root.rightchild)
Preorder(root)

'''Here we are calling the root at the end'''
def Postorder(root):
    if root:
        Postorder(root.leftchild)
        Postorder(root.rightchild)
        print(root.rootdata)
Postorder(root)
        












