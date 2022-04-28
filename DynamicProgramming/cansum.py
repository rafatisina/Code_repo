#LeetCode
def cansum(target: int, lst, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True
    if target < 0:
        return False
    for v in lst:
        remainder = target - v
        if cansum(remainder, lst, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False


result = cansum(3500, [4, 2])
print(result)
