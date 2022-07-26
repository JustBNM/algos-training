import sys
sys.setrecursionlimit(1000000)

# -----------------------------------------
# Решение через поддержание значения предыдущего элемента (тк in-order обход
# проходит ключи в отсортированном порядке)
n = int(input()) #число вершин
graph = [0]*n

status = 'CORRECT'
prev = float('-inf')

for i in range(n):
    key, left, right = map(int, input().split())
    graph[i] = (key, left, right)
    
# in-order (left, key, right)
def in_order(i):
    global status
    global prev
    if graph[i][1] != -1:
        in_order(graph[i][1])
    if prev > graph[i][0]:
        status = 'INCORRECT'
    prev = graph[i][0]

    if graph[i][2] != -1:
        in_order(graph[i][2])

if n == 0:
    print(status)
else:
    in_order(0)
    print(status)
# --------------------------------------------------

# Решение с поддержанием min-max для каждого поддерева:
class SearchTree:
    def __init__(self, tree):
        self.tree = tree

    def value(self, node):
        return self.tree[node][0]

    def left(self, node):
        return self.tree[node][1]

    def right(self, node):
        return self.tree[node][2]

    def check(self, node=0, min=float('-inf'), max=float('inf')):
        if node == -1:
            return True
        v = self.value(node)
        if v < min or v > max:
            return False
        return (self.check(self.left(node), min, v - 1) and
                self.check(self.right(node), v + 1, max))
    # Для проверки левого поддерева min оставляем тем же
    #                               max меняем на "значение в узле - 1"
    # Для проверки правого поддерева min меняем на "значение в узле + 1"
    #                               max оставляем тем же

def process_lines(ar):
    tree = SearchTree(ar)

    return 'CORRECT' if len(tree.tree) == 0 or tree.check() else 'INCORRECT'

graph = [0]*n
for i in range(n):
    key, left, right = map(int, input().split())
    graph[i] = (key, left, right)
    
print(process_lines(graph))