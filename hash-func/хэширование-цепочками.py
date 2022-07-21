"""
Хэширование цепочками 
https://stepik.org/lesson/41562/step/2?unit=20016

ord() переводит ascii в числовой код
"""
p = 1000000007
x=263
m=int(input()) #число ячеек в таблице 
n = int(input()) # число запросов

hash_table = [[] for _ in range(m)]

def hash(string):
    hash_val = 0 
    for i in range(len(string)):
        val = ord(string[i])
        hash_val += val*powers_x[i]
        hash_val = hash_val%p
    return hash_val%m

def add(string):
    hash_val = hash(string)
    if string not in hash_table[hash_val]:
        hash_table[hash_val].append(string)
def delete(string):
    hash_val = hash(string)
    if string in hash_table[hash_val]:
        hash_table[hash_val].remove(string)
def find(string):
    hash_val = hash(string)
    if string in hash_table[hash_val]:
        print('yes')
    else:
        print('no')
def check(i):
    print(' '.join(reversed(hash_table[i])))

powers_x = [1]
for i in range(1, 16):
    powers_x.append((powers_x[i-1]*x)%p)
    
for _ in range(n):
    command, obj = input().split()
    if command == 'add':
        add(obj)
    if command == 'del':
        delete(obj)
    if command == 'find':
        find(obj)
    if command == 'check':
        check(int(obj))