# max sum of sub-sequence
#using kaden's algorithm
lst = [4,-1,-3,6,-2,-1,3,2,-8,-2]
curr_sum = 0
max_sum = 0
for i in range(0,len(lst)):
    curr_sum = curr_sum + lst[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum = 0
        
print(max_sum)
