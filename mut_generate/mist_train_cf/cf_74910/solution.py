"""
QUESTION:
Develop a function `bell_number(n)` that calculates the nth Bell number, where n is a non-negative integer, using the concept of the Bell Triangle. The function should return the nth Bell number, which represents the number of ways to partition a set of n items into any number of subsets.
"""

def bell_number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]   # nth Bell number is the 0th element of nth row