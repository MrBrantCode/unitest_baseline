"""
QUESTION:
Write a function `column_sum` that accepts a 2D array with n rows and m columns, where 1 <= n, m <= 10^6 and elements are integers between -10^6 and 10^6. The function should return the column-wise sum of the given array without using any built-in functions or libraries. The function should have a time complexity of O(n*m) and a space complexity of O(m). If the input array is empty, the function should return an empty array.
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