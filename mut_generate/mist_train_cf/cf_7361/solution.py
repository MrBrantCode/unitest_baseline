"""
QUESTION:
Write a function `calculate_combination(n, k, M)` that calculates the combination of n elements taken k at a time, where n and k are non-negative integers and the result does not exceed the limit M. The function should return an error message if n or k is a negative integer, n is less than k, the result exceeds the limit M, or n exceeds the limit M.
"""

def entrance(n, k, M):
    # Check if n and k are non-negative integers
    if n < 0 or k < 0 or not isinstance(n, int) or not isinstance(k, int):
        return "Error: n and k must be non-negative integers"
    
    # Check if n is greater than or equal to k
    if n < k:
        return "Error: n must be greater than or equal to k"
    
    # Check if n is less than or equal to M
    if n > M:
        return "Error: n must be less than or equal to M"
    
    # Initialize result variable
    result = 1
    
    # Calculate combination using iterative approach
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
        
        # Check if the result exceeds the limit M
        if result > M:
            return "Error: Combination exceeds the limit M"
    
    return result