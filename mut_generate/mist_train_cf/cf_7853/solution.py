"""
QUESTION:
Write a function `column_sum` that takes a 2D array of integers as input and returns a 1D array containing the column-wise sum of the input array. The input array will have n rows and m columns, where 1 <= n, m <= 10^6. The elements of the array will be integers between -10^6 and 10^6. The function should not use any built-in functions or libraries to calculate the column-wise sum, should handle the case where the input array is empty, and should have a time complexity of O(n*m) and a space complexity of O(m).
"""

def column_sum(arr):
    if not arr:  
        return []
    
    rows = len(arr)
    cols = len(arr[0])
    
    result = [0] * cols  
    
    for col in range(cols):  
        for row in range(rows):  
            result[col] += arr[row][col]  
    
    return result