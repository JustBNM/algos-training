# -*- coding: utf-8 -*-
"""
https://stepik.org/lesson/41562/step/1?unit=20016
"""
n = int(input()) # Число запросов
# # Решение через словарь
phone_book = {}
for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        phone_book[command[1]] = command[2]
    if command[0] == 'del':
        if command[1] in phone_book:
            del phone_book[command[1]]
    if command[0] == 'find':
        print(phone_book.get(command[1], 'not found'))
        
         
# Решение через таблицу с прямой адресацией
n = int(input()) # Число запросов
m = 10**5
size = 10**5
phone_book = ['empty']*size
hash = lambda x: x%m

for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        key, val = command[1], command[2]
        j=0
        while (phone_book[(hash(int(key))+j)%size] != 'empty' and
            phone_book[(hash(int(key))+j)%size] != 'poped'):
            
            if phone_book[(hash(int(key))+j)%size][0] == key:
                break
            j+=1
        phone_book[(hash(int(key))+j)%m] = (key, val)
        
    if command[0] == 'del':
        key = command[1]
        j=0
        while (phone_book[(hash(int(key))+j)%size] != 'empty' and
            phone_book[(hash(int(key))+j)%size][0] != key):
            j+=1
        if phone_book[(hash(int(key))+j)%size][0] == key:
            phone_book[(hash(int(key))+j)%size] = 'poped'
    if command[0] == 'find':
        key = command[1]
        j=0
        while (phone_book[(hash(int(key))+j)%size] != 'empty' and
            phone_book[(hash(int(key))+j)%size][0] != key):
            j+=1
        if phone_book[(hash(int(key))+j)%size][0] == key:
            print(phone_book[(hash(int(key))+j)%size][1])
        else:
            print('not found')
