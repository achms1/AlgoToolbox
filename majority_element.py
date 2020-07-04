# Uses python3
import sys

def get_majority_element(a, left, right):
    r = 0
    l = 0
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    le = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    re = get_majority_element(a, (left + right - 1) // 2 + 1, right)
    for i in range(left, right):
        if a[i] == re:
            r += 1
    if r > (right - left) // 2:
        return re
    for i in range(left, right):
        if a[i] == le:
            l += 1
    if l > (right - left) // 2:
        return le
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
