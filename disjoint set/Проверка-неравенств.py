'''
https://stepik.org/lesson/41560/step/4?unit=20013'''
n, e, d = map(int, input().split()) 
# число переменных, равенств и неравенств соответсвенно

class DisjointSet:
    def __init__(self, n):
        self.parents = range(n)
        self.rank = [0]*n
    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i
    def union(self, i, j):
        i_id, j_id = self.find(i), self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parents[j_id] = i_id
        else:
            self.parents[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id]+=1
my_set = DisjointSet(n)
break_flag = False
# union для равенств:
for _ in range(e):
    i, j = map(int, input().split())
    my_set.union(i-1, j-1)
# Проверка для неравенств:
for _ in range(d):
    i, j = map(int, input().split())
    print(my_set.find(i-1), my_set.find(j-1))
    if my_set.find(i-1) == my_set.find(j-1):
        break_flag = True
        break
if break_flag: print(0)
else: print(1)

'''
Sample Input 2:

4 6 1
1 2
1 3
1 4
2 3
2 4
3 4
1 2
Sample Output 2:

0
'''