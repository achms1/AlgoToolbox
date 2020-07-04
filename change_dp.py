# Uses python3
import sys

def get_change(m):
    #write your code here
    changes = []
    changes.append(0)
    coins = [1,3,4]
    for i in range(1,m+1):
        maxi = 999999
        for item in coins:
            if i - item >= 0:
                temp = changes[i-item]+1
                if temp < maxi:
                    maxi = temp
        changes.append(maxi)
    return changes[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
