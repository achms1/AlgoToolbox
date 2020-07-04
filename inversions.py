# Uses python3
import sys

def merging(a, b, left, avge, right):
    cout = 0
    x, y, z = left, avge, left
    while x <= avge - 1 and y <= right:
        if a[x] <= a[y]:
            b[z] = a[x]
            x += 1
        else:
            b[z] = a[y]
            y += 1
            inv_count += avge - x
        z += 1
    while x <= avge - 1:
        b[z] = a[x]
        x += 1
        z += 1
    while y <= right:
        b[z] = a[y]
        y += 1
        z += 1
    for x in range(left, right + 1):
        a[x] = b[x]
    return cout
    
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right > left:
        return number_of_inversions
    avge = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, avge)
    number_of_inversions += get_number_of_inversions(a, b, avge+1, right)
    number_of_inversions += merging(a, b, left, avge+1, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
