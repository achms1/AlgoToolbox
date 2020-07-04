# Uses python3
import sys

def get_change(m):
    #write your code here
    k = m//10 + (m%10)//5 + (m%5)
    return k

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
