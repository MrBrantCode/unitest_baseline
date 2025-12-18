"""
QUESTION:
Implement the function `sqrt(n)` to calculate the square root of a given positive integer `n` and round it to the nearest integer. The function should handle input numbers up to 10^18, have a time complexity of O(log(N)), and return the result as a string representation without using any built-in math libraries or functions.
"""

def sqrt(n):
    low = 0
    high = n
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid * mid == n:
            return str(mid)
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1
    
    return str(high)