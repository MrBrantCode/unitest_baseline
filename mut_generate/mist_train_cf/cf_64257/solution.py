"""
QUESTION:
Create a function `longest_subarray(array)` that finds the longest subarray with an equal number of 0's and 1's in a given 2-dimensional array. The subarray can be in any straight direction: horizontal, vertical, or diagonal. The array only contains 0's and 1's. Return the longest subarray with an equal number of 0's and 1's.
"""

def longest_subarray(array):
    longest_subarray = []
    n = len(array)
    m = len(array[0])

    def dfs(i, j, current_subarray, dir):
        nonlocal longest_subarray, n, m
        if i < 0 or i >= n or j < 0 or j >= m:
            return 
        current_subarray.append(array[i][j])
        zeros = current_subarray.count(0)
        ones = current_subarray.count(1)
        if zeros == ones and len(current_subarray) > len(longest_subarray):
            longest_subarray = current_subarray[:]
        if dir == 'h':
            dfs(i, j+1, current_subarray, 'h')
        elif dir == 'v':
            dfs(i+1, j, current_subarray, 'v')
        elif dir == 'd':
            dfs(i+1, j+1, current_subarray, 'd')
        current_subarray.pop()

    for i in range(n):
        for j in range(m):
            dfs(i, j, [], 'h')
            dfs(i, j, [], 'v')
            dfs(i, j, [], 'd')
    
    return longest_subarray