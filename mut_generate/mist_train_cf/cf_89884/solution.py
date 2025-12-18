"""
QUESTION:
Implement a function `calculate_combination(n, k, M)` that calculates the combination of `n` elements taken `k` at a time, where `n` and `k` are non-negative integers and `M` is a specified limit. The function should return the calculated combination if it does not exceed the limit `M`; otherwise, it should return an error message. The function should also handle cases where `n` or `k` is invalid (not a non-negative integer) or where `n` is less than `k`.
"""

def calculate_combination(n, k, M):
    """
    Calculates the combination of n elements taken k at a time without exceeding a specified limit M.

    Args:
    n (int): The total number of elements.
    k (int): The number of elements to choose.
    M (int): The specified limit.

    Returns:
    int: The calculated combination if it does not exceed the limit M, otherwise an error message.
    """

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