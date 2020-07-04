# Uses python3
import math
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minandmax(M,m,i,j,op):
    mini = math.inf
    maxi = -math.inf
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
    return mini, maxi

def get_maximum_value(operands, operators):
    #write your code here
    l = len(operands)
    m = [[None for x in range(l)] for x in range(l)]
    M = [[None for x in range(l)] for x in range(l)]

    for i in range(l):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, l):
        for i in range(0, l-s):
            j = i + s
            m[i][j], M[i][j] = minandmax(M, m, i, j, operators)

    return M[0][l-1]

if __name__ == "__main__":
    dataset = input()
    operators, operands = [], []
    for i in dataset:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            operands.append(int(i))

    print(get_maximum_value(operands, operators))
