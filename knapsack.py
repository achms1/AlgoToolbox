# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def dyna_optimal(W, w):
    items = [0] + w
    weights = [[0]*(W+1) for _ in range(len(items))]
    for i in range(1,len(items)):
        for w in range(1,W+1):
            if w - items[i] < 0:
                weights[i][w] = weights[i-1][w]
            else:
                weights[i][w] = max(weights[i-1][w],(weights[i-1][w-items[i]]+items[i]))
    return weights[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(dyna_optimal(W, w))
