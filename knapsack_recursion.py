# knapsack using recursion

def calc_max(P,W,C,n):
    if n == 0 or C == 0:
        return 0
    if (W[n-1] > C):
        return calc_max(P,W,C,n-1)
    else:
        return max(P[n-1] + calc_max(P,W,C-W[n-1],n-1),calc_max(P,W,C,n-1))
        
P = [5,10,15,7,8,9,4]
W = [1,3,5,4,1,3,2]
C = 15
n = len(P)
calc_max(P,W,C,n)
