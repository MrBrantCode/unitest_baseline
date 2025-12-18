"""
QUESTION:
Implement the function `fibonacci(n: int) -> int` that takes a positive integer `n` as input and returns the Nth term of the Fibonacci sequence using dynamic programming. The function should have a time complexity of O(n) and a space complexity of O(1), and it should handle values of `n` up to 10^6 efficiently. Additionally, the function should handle negative and non-integer values of `n` gracefully and return an appropriate error message.
"""

def fibonacci(n: int) -> int:
    # Handle negative values of n
    if n < 0:
        return "Error: n must be a positive integer"
    
    # Handle non-integer values of n
    if not isinstance(n, int):
        return "Error: n must be an integer"
    
    # Handle the base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Initialize the variables for the two previous terms
    prev1 = 1
    prev2 = 0
    
    # Calculate the Nth term of the Fibonacci sequence using dynamic programming
    for i in range(2, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return current