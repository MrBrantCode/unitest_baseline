"""
QUESTION:
Write a function `maxSumPath(grid, k)` that determines the maximal possible sum of exactly `k` distinct cells within an `NxN` grid, where `N` is not less than 2. The function should return a list containing the maximum sum and a sequence of the values forming this ultimate sum path. The values in the grid are distinct and ranged between 1 and `N*N`. Visiting the same cell multiple times is allowed.
"""

def maxSumPath(grid, k):
    # Given each cell has distinct value, the maximum k cells will always be the maximum k values in the grid.
    # Flatten the grid to a list and sort it in reverse order
    values = sorted(sum(grid, []), reverse=True)
    max_values = values[:k]
    max_sum = sum(max_values)
    # Compute path which is the value itself in this case
    path = max_values

    return [max_sum, path]