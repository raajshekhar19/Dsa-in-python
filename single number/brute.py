nums = [1, 2, 2, 4, 3, 1, 4]

ans = 0
for i in range(0,len(nums)):
    k = nums[i]
    found = 0
    for j in range(i+1,len(nums)):
        if(k==nums[j]):
            found = 1
            break
    if found==0:
        ans = nums[i]
        break

print(ans)
    