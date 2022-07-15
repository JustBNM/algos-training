# test input:
# 10
# 9 7 5 5 2 9 9 9 2 -1
# test output:
# 4

from collections import defaultdict

n = int(input()) # number of nodes
# массив с предком для каждой из вершин
array = list(map(int, input().split())) 

# Построим граф на adjacent list
# Пройдёмся по нему с помощью BFS
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addNode(self, u, v):
        self.graph[u].append(v)
    def bfs(self):
        visited = {root_ind: 1}
        queue = [(root_ind, 1)]
        max_height = 0
        
        while queue:
            node, height = queue.pop(0)
            max_height = max(max_height, height)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited[neighbor] = 1
                    queue.append((neighbor, height+1))
        return max_height

g = Graph()
for ind, val in enumerate(array):
    if val == -1:
        root_ind = ind
    else:
        g.addNode(val, ind)
height = g.bfs()
print(height)