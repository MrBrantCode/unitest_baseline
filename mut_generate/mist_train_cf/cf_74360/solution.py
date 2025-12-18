"""
QUESTION:
Create two functions, `is_even(n)` and `is_odd(n)`, that use mutual recursion to determine whether a given number `n` is even or odd. Ensure the functions handle all non-negative integer inputs and include base cases to terminate the recursive loop.
"""

def entrance(n):
    def is_even(x):
        if x == 0:
            return True
        else:
            return is_odd(x-1)

    def is_odd(x):
        if x == 0:
            return False
        else:
            return is_even(x-1)

    return is_even(n)

# I have excluded the test case in the reorganized answer.