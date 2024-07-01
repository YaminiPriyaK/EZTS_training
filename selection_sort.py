# selection sort

l = list(map(int,input("Enter the numbers to be sorted:").split()))
for j in range(0,len(l)):
    pos = j
    min = l[j]
    for i in range(j,len(l)):
        if l[i] < min:
            min = l[i]
            pos = i
    l[j],l[pos] = l[pos],l[j]
    
print(l)
