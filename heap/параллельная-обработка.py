# -*- coding: utf-8 -*- 
'''
По данным n процессорам и m задач определите, для каждой из задач,
каким процессором она будет обработана.

Вход. Число процессоров n и последовательность чисел
t0, . . . , tm−1, где ti — время, необходимое на обработку i-й
задачи.

Выход. Для каждой задачи определите, какой процессор
и в какое время начнёт её обрабатывать, предполагая, что
каждая задача поступает на обработку первому освободившемуся процессору
'''

n, m = map(int, input().split()) # Число процессоров и задач
tasks = list(map(int, input().split()))

heap = [[0,i] for i in range(n)]

def shiftDown(i):
    minIndex = i
    if i*2+1 < n and heap[i*2+1] < heap[minIndex]:
        minIndex = i*2+1
    if i*2+2 < n and heap[i*2+2] < heap[minIndex]:
        minIndex = i*2+2
    if minIndex != i:
        heap[minIndex], heap[i] = heap[i], heap[minIndex]
        shiftDown(minIndex)

for task in tasks:
    print(heap[0][1], heap[0][0])
    heap[0][0] += task
    shiftDown(0)
    
# Решение с использованием встроенной библиотеки heapq
from heapq import heappush, heappop

n, m = map(int, input().split()) # Число процессоров и задач
tasks = list(map(int, input().split()))
heap = [(0,i) for i in range(n)]

for task in tasks:
    start, cpu = heappop(heap)
    print(cpu, start)
    heappush(heap, (start+task, cpu))
    
'''
Sample Input:

2 5
1 2 3 4 5
Sample Output:

0 0
1 0
0 1
1 2
0 4
'''