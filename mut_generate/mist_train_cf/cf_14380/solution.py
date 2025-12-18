"""
QUESTION:
Write a function called `column_wise_sum` that takes a 2D array as input and returns a list containing the sum of each column. The input array will have between 1 and 10^3 rows and columns, and each element will be an integer between -10^3 and 10^3. The function should not use any built-in sum functions or libraries, and it should be optimized for large input arrays.
"""

def column_wise_sum(arr):
    n = len(arr)
    m = len(arr[0])
    result = [0] * m
    
    for j in range(m):
        for i in range(n):
            result[j] += arr[i][j]
    
    return result