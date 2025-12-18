"""
QUESTION:
Implement a function `compute_factorial(n)` to calculate the factorial of a given positive integer `n` using a loop structure. The function should handle the following cases: 
- If `n` is negative, print "Error: The number must be a positive integer." and return `None`.
- If `n` is greater than 20, print "Error: The number is too large to compute factorial." and return `None`.
- If `n` is not an integer, print "Error: The number must be an integer." and return `None`.
- If `n` is zero, return 1.
- Otherwise, return the calculated factorial of `n`.
"""

def compute_factorial(n):
    # Check if number is negative
    if n < 0:
        print("Error: The number must be a positive integer.")
        return None

    # Check if number is greater than 20
    if n > 20:
        print("Error: The number is too large to compute factorial.")
        return None

    # Check if number is not an integer
    if not isinstance(n, int):
        print("Error: The number must be an integer.")
        return None

    # Handle the case where number is zero
    if n == 0:
        return 1

    factorial = 1

    # Compute the factorial using a loop structure
    for i in range(1, n+1):
        factorial *= i

    return factorial