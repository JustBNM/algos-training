n = int(input()) # длина массива
array = list(map(int, input().split()))
m = int(input()) # размер окна

# Реализуем очередь, через 2 стека, при этом будем поддерживать в нём максимум
def reverse_stack_with_max(stack):
    global_max = 0
    reversed_stack = []
    while stack:
        val = stack.pop()
        if type(val) != type(int()):
            val, _ = val
        if val > global_max:
            global_max = val
        reversed_stack.append((val, global_max))
    return reversed_stack

answer = []

input_stack = []
output_stack = reverse_stack_with_max(array[:m])

for i in range(m, n ):
    current_max = output_stack.pop()[1]
    if input_stack:
        current_max = max(current_max, input_stack[-1][1])
        input_stack += [(array[i], max(array[i], input_stack[-1][1]))]
    else:
        input_stack += [(array[i], array[i])]
    answer+= [current_max]
    
    if not output_stack:
        output_stack = reverse_stack_with_max(input_stack)
        input_stack = []

current_max = output_stack.pop()[1]
if input_stack:
    current_max = max(current_max, input_stack[-1][1])
answer+= [current_max]

print(' '.join(map(str, answer)))

# test input:
# 8 
# 2 7 3 1 5 2 6 2
# 4
# test output
# 7 7 5 6 6