# -*- coding: utf-8 -*-
# На самом деле в данной задаче достаточно поддерживать только стек 
# с максимумами
class Stack:
    def __init__(self):
        self.stack = []
        self.s_max = []
    def push(self, val):
        self.stack.append(val)
        if self.s_max:
            current_max = max(self._stack_max(), val)
            self.s_max.append(current_max)
        else:
            self.s_max.append(val)
    def pop(self):
        self.stack.pop()
        self.s_max.pop()
    def _stack_max(self):
        return self.s_max[-1]
    def stack_max(self):
        print(self.s_max[-1])

stack = Stack()

q = int(input()) #число запросов
for _ in range(q):
    query = input()
    if query == 'pop':
        stack.pop()
    elif query == 'max':
        stack.stack_max()
    else:
        query = query.split()
        stack.push(int(query[-1]))
        
# test input:
'''
5
push 1
push 2
max
pop
max
'''
#test output:
'''
2
1
'''
        