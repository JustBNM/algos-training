'https://stepik.org/lesson/41560/step/3?unit=20013'

n, m = map(int, input().split()) # число таблиц и число запросов
sizes = list(map(int, input().split())) # размеры таблиц

class DisjointSet:
    def __init__(self, n, sizes):
        'Создаём синглтоны, каждый элемент - это отдельный сет'
        self.parent = [i for i in range (n)]
        self.size = sizes
        self.rank = [0]*n
        self.max_size = max(sizes)
    def find(self, i):
        'поиск id элемента, т.е. корневого элемента'
        if self.parent[i] != i:
            i = self.find(self.parent[i])
        return i
    def union(self, i, j):
        'объединение множеств'
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            print(self.max_size)
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            self.size[i_id] += self.size[j_id]
            self.max_size = max(self.max_size, self.size[i_id])
        else:
            self.parent[i_id] = j_id
            self.size[j_id] += self.size[i_id]
            self.max_size = max(self.max_size, self.size[j_id])
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
        print(self.max_size)
        
my_set = DisjointSet(n, sizes)
for _ in range(m):
    destination, source = map(int, input().split()) # номера таблиц 
                                                    # для объединения
                                                    
    my_set.union(destination-1, source-1)
    
'''
Sample Input:

5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3
Sample Output:

2
2
3
5
5
'''