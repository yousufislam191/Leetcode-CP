accounts = [[1, 5], [7, 3], [3, 5]]
for i in range(len(accounts)):
    wealth = [sum(x) for x in accounts]

print(max(wealth))
