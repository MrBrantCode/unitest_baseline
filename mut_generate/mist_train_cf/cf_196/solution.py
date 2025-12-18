"""
QUESTION:
Write a function `sqrt(n)` that calculates the square root of a given positive integer `n` and rounds it to the nearest integer, without using any built-in math libraries or functions. The function should be able to handle input numbers up to 10^18 and return the result as a string representation. The time complexity of the solution should be O(log(N)).
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