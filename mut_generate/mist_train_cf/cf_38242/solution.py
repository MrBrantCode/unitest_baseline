"""
QUESTION:
Implement a function named `last_fibonacci` that takes an integer `x` as input and returns the last number in the Fibonacci sequence up to the given index `x`. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. If the input `x` is negative, the function should print "Invalid input" and return without a value.
"""

def last_fibonacci(x: int) -> int:
    if x < 0:
        print("Invalid input")
        return
    
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, x + 1):
        a, b = b, a + b
    
    return b