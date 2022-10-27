nums = [2, 5, 1, 3, 4, 7]
n = 3

result = [j for i in zip(nums[0:n], nums[n: len(nums)]) for j in i]
print(result)
