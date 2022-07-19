# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:56:14 2022

@author: pavel.rachitskiy
"""

class Solution:
    def __init__(self):
        self.memo = {0: 0, 1:1}
    def fib(self, n: int) -> int:
        if n not in self.memo.keys():
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]