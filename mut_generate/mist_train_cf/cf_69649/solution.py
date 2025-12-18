"""
QUESTION:
Write a function `invert(arr)` that takes a two-dimensional array as input and returns a new array with the order of both rows and columns inverted, without using any predefined or built-in methods. The time complexity of the solution should be within O(n²).
"""

def invert(arr):
    result = [] 
    for i in range(len(arr)-1, -1, -1): 
        temp = [] 
        for j in range(len(arr[i])-1, -1, -1): 
            temp.append(arr[i][j])
        result.append(temp) 
    return result