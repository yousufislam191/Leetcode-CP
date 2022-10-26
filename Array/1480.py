ans = []
temp = []
nums = [int(item) for item in input("Enter the list items : ").split()]
length = len(nums)
for i in range(length):
    temp.append(nums[i])
    ans.append(sum(temp))

print("temp: ", temp)
print("ans: ", ans)
