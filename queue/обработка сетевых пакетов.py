# -*- coding: utf-8 -*-
buffer_size, n_package = map(int, input().split())

queue = []
for i in range(n_package):
    arrival, duration = map(int, input().split())
    
    while queue and queue[0] <= arrival:
        queue.pop(0)
    if len(queue) < buffer_size:
        if queue != []:
            start_processing = max(queue[-1], arrival)
        else:
            start_processing = arrival
        queue.append(start_processing + duration)
        print(start_processing)
    else:
        print(-1)
            