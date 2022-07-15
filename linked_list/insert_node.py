# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 00:49:38 2022

@author: pavel.rachitskiy
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        new_head = Node(x)
        new_head.next = head
        return new_head
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        temp = head
        while temp.next:
            temp = temp.next
        new_node = Node(x)
        temp.next = new_node
        return head
    
sol = Solution()

head = Node(8)
head = sol.insertAtBegining(head, 8)
print(head)
#8 1 8 0 7 0 2 0 6 1 6 0 2 0 1 0 2 0 7 0