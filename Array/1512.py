nums = [1, 2, 3, 1, 1, 3]

result = [(i, j) for index, i in enumerate(nums)
          for j in nums[index+1:] if i == j]
print(len(result))
