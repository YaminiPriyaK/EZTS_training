#Bubble Sort

L=list(map(int,input().split()))
n=len(L)
for j in range(0,n):
    for i in range(0,n-1-j):
        if L[i]>L[i+1]:
            L[i],L[i+1]=L[i+1],L[i]

print(L)