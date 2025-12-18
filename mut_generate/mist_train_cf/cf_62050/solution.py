"""
QUESTION:
Given an array `A` (index starts at `1`) consisting of N integers: A1, A2, ..., AN and two integers `B` and `C`, where B denotes the maximum number of steps that can be jumped from any index `i` to any index `j` in the range `i+1` to `i+B`, and C denotes the maximum number of jumps allowed. The aim is to find the path of indexes (starting from 1 to N) in the array to reach the place indexed `N` using the minimum coins and not exceeding the maximum number of jumps. If there are multiple paths with the same cost and number of jumps, return the lexicographically smallest such path. 

The function `cheapestJump` should take as input an array `A`, and integers `B` and `C`, and return the path of indexes to reach the place indexed `N`. The array `A` has a length in the range of [1, 1000], `B` is in the range of [1, 100], `C` is in the range of [1, 100], and each element in `A` is in the range of [-1, 100]. If it's not possible to reach the place indexed `N` within the maximum number of jumps or if the cost exceeds the minimum, then return an empty array.
"""

def cheapestJump(A, B, C):
    size = len(A)
    next_jump = [-1]*size
    dp = [float('inf')]*size
    dp[-1] = A[-1]
    steps = [0]*size
    
    for i in range(size - 1, -1, -1):
        for b in range(1, B + 1):
            if i + b < size and A[i + b] != -1 and steps[i + b] + 1 <= C:
                if A[i] + dp[i + b] < dp[i] or (A[i] + dp[i + b] == dp[i] and (next_jump[i] == -1 or i + b < next_jump[i])):
                    dp[i] = A[i] + dp[i + b]
                    next_jump[i] = i + b
                    steps[i] = steps[i + b] + 1

    if dp[0] == float('inf'):
        return []

    i, path = 0, []
    while i != -1:
        path.append(i + 1)
        i = next_jump[i]
    return path