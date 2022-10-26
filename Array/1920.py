ans = []
nums = [int(item) for item in input("Enter the list items : ").split()]
length = len(nums)
for i in range(length):
    ans.append(nums[nums[i]])
print(ans)
