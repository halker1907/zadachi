expr = input().split(" * ")
for i in range(len(expr)):
    if "-" in expr[i]:
        nums = expr[i][1:-1].split(" - ")
        expr[i] = nums[0] - nums[1]
print()