# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 02:17:01 2022

@author: pavel.rachitskiy
"""

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# DFS-подобные способы обойти дерево
#Function to return a list containing the inorder traversal of the tree.
# used in Binary Search Trees (BST) 
class Solution:
    def InOrder(self,root):
        result = []
        if root is None:
            return []
        result += self.InOrder(root.left)
        result += [root.data]
        result += self.InOrder(root.right)
        return result

#Function to return a list containing the preorder traversal of the tree.
# is used to create a copy of tree
def preorder(root):
    result = []
    if root is None:
        return []
    result += [root.data]
    result += preorder(root.left)
    result += preorder(root.right)
    return result

#Function to return a list containing the postorder traversal of the tree.
# is used to delete tree
def postOrder(root):
    result = []
    if root is None:
        return []
    result += postOrder(root.left)
    result += postOrder(root.right)
    result += [root.data]
    return result

#BFS-подобный способ обойти дерево (level-order):
#Function to return the level order traversal of a tree.
def levelOrder(self,root):
    answer = []
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        answer += [node.data]
        if node.left is not None:
            queue += [node.left]
        if node.right is not None:
            queue += [node.right]
    return answer


