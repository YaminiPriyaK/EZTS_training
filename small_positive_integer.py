#find smallest positive integer in an array
arr=[5,7,-10,-3,0,3,-5,1]
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]<min and arr[i]>=1:
        min=arr[i]
print(min)
