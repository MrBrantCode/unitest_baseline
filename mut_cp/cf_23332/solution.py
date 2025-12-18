"""
ORIGINAL QUESTION:
Create a function named `fibonacci` that generates the Fibonacci sequence. The function should take an integer `n` as input and return the `n`-th Fibonacci number. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. If `n` is less than 0, the function should print "Incorrect input".
"""

def fibonacci(n): 
    """
    Generates the nth Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to generate.

    Returns:
        int: The nth Fibonacci number if n is non-negative, otherwise prints "Incorrect input".
    """
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b