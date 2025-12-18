"""
QUESTION:
Given an n x n binary grid, return the minimum number of steps needed to make the grid valid by swapping adjacent rows according to the rules: the row being moved upwards has more 1's than the row it is replacing, and the row being moved downwards has fewer 1's than the row it is replacing. A grid is valid if all the cells above the main diagonal are zeros. If the grid cannot be valid, return -1. The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n). The constraints are 1 <= n <= 200 and grid[i][j] is 0 or 1. Write a function named minSwaps to solve this problem.
"""

def minSwaps(grid):
    n = len(grid)
    ones = [0]*n
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                ones[i] = n-j-1    # compute number of trailing ones in each row
    steps = 0
    for i in range(n):
        swap = -1
        for j in range(i,n):
            if ones[j] >= n-i-1:   # find row with enough trailing zeros
                swap = j
                break
        if swap == -1:
            return -1
        while swap > i:  # bring the row upwards
            ones[swap], ones[swap-1] = ones[swap-1], ones[swap]   
            swap -= 1
            steps += 1
    return steps