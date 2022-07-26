# -*- coding: utf-8 -*-
"""
https://stepik.org/lesson/45970/step/1?unit=24123
"""

n = int(input()) #число вершин
graph = [0]*n

for i in range(n):
    key, left, right = map(int, input().split())
    graph[i] = (key, left, right)
    
#in-order (left, key, right)
def in_order(i):
    if graph[i][1] != -1:
        in_order(graph[i][1])
    print(graph[i][0], end = ' ')
    if graph[i][2] != -1:
        in_order(graph[i][2])
in_order(0)
print()

#pre-order (key, left, right)
def pre_order(i):
    print(graph[i][0], end = ' ')
    if graph[i][1] != -1:
        pre_order(graph[i][1])
    if graph[i][2] != -1:
        pre_order(graph[i][2])
pre_order(0)
print()

#post-order (left, right, key)
def post_order(i):
    if graph[i][1] != -1:
        post_order(graph[i][1])
    if graph[i][2] != -1:
        post_order(graph[i][2])
    print(graph[i][0], end = ' ')
post_order(0)
print()    