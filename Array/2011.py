operations = ["--X", "X++", "X++"]
operationsDictonary = {
    "--X": -1,
    "X--": -1,
    "++X": 1,
    "X++": 1
}
result = sum(operationsDictonary[i] for i in operations)
print(result)
