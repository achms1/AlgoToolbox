# Uses python3
def edit_distance(s, t):
    # # i = len(s)
    # # j = len(t)
    # if not (i,j) in T:
    #     if i == 0:
    #         T[i,j] = j
    #     elif j == 0:
    #         T[i,j] = i
    #     else:
    #         if s[i-1] == t[j-1]:
    #             diff = 0
    #         else:
    #             T[i,j] = min(edit_distance(a,b,i-1,j)+1,edit_distance(a,b,i,j-1)+1,edit_distance(a,b,i-1,j-1)+diff)
    # return T[i,j]
    T = [[x]+[0]*(len(t)) for x in range (len(s)+1)]
    T[0] = [x for x in range(len(t)+1)]
    for i in range(len(s)+1):
        T[i][0] = i
    for j in range(len(t)+1):
        T[0][j] = j
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = min(T[i-1][j],T[i][j-1],T[i-1][j-1])+1
    return T[-1][-1]
if __name__ == "__main__":
    print(edit_distance(input(),input()))
