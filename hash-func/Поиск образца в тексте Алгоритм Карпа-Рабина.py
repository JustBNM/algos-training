# -*- coding: utf-8 -*-
"""
https://stepik.org/lesson/41562/step/3?unit=20016
"""
substring = input()
string = input()

p = 1000000007
x=263

x_powers = [1]
for i in range(1,len(substring)):
    x_powers.append((x_powers[i-1]*x)%p)
    
def hash(string):
    hash_val = 0
    for i in range(len(string)):
        val = ord(string[i])
        hash_val+=val*x_powers[i]
        hash_val = hash_val%p
    return hash_val

def check_eq(sample, substring):
    if sample == substring:
        answer.append(i)

target_hash = hash(substring)

sample = string[len(string)-len(substring):]
sample_hash = hash(sample)
answer = []
i = len(string)-len(substring)
check_eq(sample, substring)
while i != 0:
    i-=1
    sample_hash = ((sample_hash-(ord(sample[-1])*x_powers[len(substring)-1]))*x
                   +ord(string[i]))%p
    sample = string[i] + sample[:-1]
    if sample_hash == target_hash:
        check_eq(sample, substring)

print(' '.join(list(map(str, reversed(answer)))))