#Uses python3

import sys

def isgreater(digi,maxi):
    return int(str(digi)+str(maxi))>=int(str(maxi)+str(digi))

def largest_number(a):
    #write your code here
    ans = []
    while a!=[]:
        maxi = 0
        for digi in a:
            if isgreater(digi, maxi):
                maxi = digi
        ans.append(maxi)
        a.remove(maxi)
    res = ""
    for x in ans:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
