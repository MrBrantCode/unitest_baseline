"""
QUESTION:
Implement a function `foo(x, y)` that takes two integers `x` and `y` as input, and returns the result after performing a series of operations based on the value of `y`. If `y` is positive, add all even numbers from 0 to `y-1` to `x`. If `y` is negative, multiply `x` by all even numbers from 0 to `-y-1`. The function should have a time complexity of O(n) where n is the absolute value of `y`, and a space complexity of O(1).
"""

def foo(x, y):
    """
    This function performs a series of operations based on the value of y.
    If y is positive, it adds all even numbers from 0 to y-1 to x.
    If y is negative, it multiplies x by all even numbers from 0 to -y-1.
    
    Time complexity: O(n) where n is the absolute value of y
    Space complexity: O(1)
    """
    if y > 0:
        for i in range(y):
            if i % 2 == 0:
                x += i
    else:
        for i in range(-y):
            if i % 2 == 0:
                x *= i
    return x