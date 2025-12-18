"""
QUESTION:
Create a function named `square_range` that takes two integers `n` and `m` where `m > n`, `1 <= n, m <= 10^9`, and `n` and `m` are positive integers. The function should return a list containing the squares of numbers from `n` to `m` (inclusive) in descending order. The function should have a time complexity of O(m - n) and should handle cases where `n` and `m` are equal or `m` is less than `n`. If `m` is less than `n`, the function should return an empty list.
"""

def square_range(n, m):
    # Validate that n and m are positive integers
    if not isinstance(n, int) or not isinstance(m, int) or n <= 0 or m <= 0:
        return "Error: n and m must be positive integers"
    
    # Ensure that n and m are within the range of 1 to 10^9
    if n > 10**9 or m > 10**9:
        return "Error: n and m must be within the range of 1 to 10^9"
    
    # Handle cases where n and m are equal
    if n == m:
        return [n**2]
    
    # Handle cases where m is less than n
    if m < n:
        return []
    
    # Calculate the squares of the numbers from n to m
    return [i**2 for i in range(m, n-1, -1)]