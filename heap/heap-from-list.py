"""
Построение кучи in place из входного массива
https://stepik.org/lesson/41235/step/6?unit=19819
10:30
"""
n = int(input()) # Число узлов в куче
nodes = list(map(int, input().split())) # Узлы

def parent_id(i):
    return (i-1)//2 if i != 0 else 0
def leftChild(i):
    return i*2 + 1
def rightChild(i):
    return i*2 + 2

counter, answer = 0, []
def buildHeap(array, n):
    def _shiftDown(array, i, size):
        global answer
        global counter
        min_ind = i
        
        left_child = leftChild(i)
        if left_child < size and array[left_child] < array[min_ind]:
            min_ind = left_child
            
        right_child = rightChild(i)
        if right_child < size and array[right_child] < array[min_ind]:
            min_ind = right_child
        if min_ind != i:
            counter+=1
            array[min_ind], array[i] = array[i], array[min_ind]
            answer += [[i, min_ind]]
            _shiftDown(array, min_ind, size)
    
    for i in range(n//2, -1, -1):
        _shiftDown(array, i, n)
             
buildHeap(nodes, n) 
print(counter)
for val in answer:
    print(' '.join(map(str, val)), end = '\n')