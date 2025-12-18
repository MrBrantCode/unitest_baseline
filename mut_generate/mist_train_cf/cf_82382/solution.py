"""
QUESTION:
Create a function named `recursive_function` that takes an integer `j` as a parameter. The function should return a list of numbers from `j` to 1 (inclusive if `j` is even, or `j-1` to 1 if `j` is odd) in descending order, decrementing by 2 at each step. If `j` is odd and greater than 1, adjust `j` to `j-1` before generating the list. The function should handle edge cases, including when `j` is an odd number or less than 1.
"""

def recursive_function(j):
    if j % 2 != 0 and j > 1:
        j -= 1
        
    result = []
    
    def recursion(k):
        if k < 1:
            return
        else:
            result.append(k)
            recursion(k-2)
    
    recursion(j)
    
    return result