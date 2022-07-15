# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:31:12 2022

@author: pavel.rachitskiy
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addNode(self, u, v):
        self.graph[u].append(v)
        
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        'V - число узлов, adj - лист смежности'
        visited = [0]*V
        visited[0] = True
        queue = [0]
        output = []
        while queue:
            node = queue.pop(0)
            output.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return output
    
g = Graph()
g.addNode(5, 4)
g.addNode(0, 1)
g.addNode(0, 2)
g.addNode(0, 3)
g.addNode(2, 4)

out = g.bfsOfGraph(5, g.graph)
print(out)