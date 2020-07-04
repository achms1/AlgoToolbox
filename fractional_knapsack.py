# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    a = []
    a = [float(v)/float(w) for v, w in zip(values,weights)]
    for _ in range(len(weights)+1):
        if capacity == 0:
            return value
            break
        maxi = max(a)
        pos = a.index(maxi)
        a[pos] = -1
        addi = min(capacity, weights[pos])
        weights[pos] -= addi
        value += addi * maxi
        capacity -= addi
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
