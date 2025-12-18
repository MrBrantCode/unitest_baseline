"""
QUESTION:
Compute the big-O time complexity for the given factorial function:
def factorial(n):
    if n == 0: 
        return 1
    else: 
        return n*factorial(n-1)
 
The function should be analyzed to determine its time complexity, including any potential drawbacks and alternative approaches.
"""

def factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)