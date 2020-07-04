# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def party(A):
    total = sum(A)
    if total % 3 != 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    A = data[1:]
    print(party(A))

