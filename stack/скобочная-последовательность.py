# Реализация стека через linkedList
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
class Stack:
    def __init__(self):
        self.stack = None
        self.head = None
    def pop(self):
        self.output = self.stack.val
        self.stack = self.stack.next
        return self.output
    def push(self, val):
        self.test = 'asdas'
        self.head = Node(val)
        self.head.next = self.stack
        self.stack = self.head
    def printStack(self):
        node = self.stack
        while node:
            print(node.val)
            node = node.next
    def isEmpty(self):
        return self.stack is None
            
# stack = Stack()
#stack.push((5, 1))
# stack.push((10, 2))
#stack.push((15, 3))
#stack.printStack()
#print('out = ',stack.pop())
# stack.printStack()
# print(stack.isEmpty())

def check(string):
    stack = Stack()
    braces = {')': '(', '}': '{', ']': '['}
    for i, val in enumerate(list(string)):
        if val not in '[]{}()':
            continue
        if val in '([{':
            stack.push((val, i+1))
        else:
            if stack.isEmpty():
                return (i+1)
            last_elem, index = stack.pop()
            if val in braces.keys() and braces[val] != last_elem:
                return(i+1)
    if stack.isEmpty():
        return 'Success'
    else:
        while not stack.isEmpty():
            last_elem, index = stack.pop()
        return index
print(check(input()))