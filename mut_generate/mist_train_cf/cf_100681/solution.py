"""
QUESTION:
Find the function `find_subset(numbers, target_sum)` that takes a list of numbers and a target sum as input, and returns a subset of the numbers that sum up to the target sum, using each number at most once. The function should be optimized for time complexity.
"""

def find_subset(numbers, target_sum):
    n = len(numbers)
    table = [[False] * (target_sum+1) for _ in range(n+1)]
    table[0][0] = True
    for i in range(1, n+1):
        for j in range(target_sum+1):
            table[i][j] = table[i-1][j]
            if j >= numbers[i-1]:
                table[i][j] |= table[i-1][j-numbers[i-1]]
    if not table[n][target_sum]:
        return None
    subset = []
    i, j = n, target_sum
    while i > 0 and j > 0:
        if table[i-1][j]:
            i -= 1
        else:
            subset.append(numbers[i-1])
            j -= numbers[i-1]
            i -= 1
    return subset