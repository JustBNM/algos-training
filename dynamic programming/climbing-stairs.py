# -*- coding: utf-8 -*-
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top?

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def __init__(self):
        self.memo = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]
    
    # with O(1) memory:
    def climbStairs_(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a