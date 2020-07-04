# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

# def dynamic_sequence(n):
#     operations = [0]
#     operations.append(1)
#     for i in range(2,n+1):
#         maxi = 99999
#         if operations[i-1] < maxi:
#             maxi = operations[i-1]
#         if i % 3 == 0:
#             if operations[i/3] < maxi:
#                 maxi = operations[i/3]
#         if  i%2 == 0:
#             if operations[i/2] < maxi:
#                 maxi = operations[i/2]
#         operations.append(temp+1)
#     return reversed(operations)

def dynamic_sequence(n):
    operations = [0] * (n + 1)
    operations[1] = 1
    for i in range(2, n + 1):
        count = [i - 1]
        if i % 2 == 0:
            count.append(i // 2)
        if i % 3 == 0:
            count.append(i // 3)
        minc = min([operations[k] for k in count])
        operations[i] = minc + 1
    current = n
    valu = [current]
    while current != 1:
        option = [current - 1]
        if current % 2 == 0:
            option.append(current // 2)
        if current % 3 == 0:
            option.append(current // 3)
        current = min([(c, operations[c]) for c in option],key=lambda x: x[1])[0]
        valu.append(current)
    return reversed(valu)

input = sys.stdin.read()
n = int(input)
sequence = list(dynamic_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
