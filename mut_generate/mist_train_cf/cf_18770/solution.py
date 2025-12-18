"""
QUESTION:
Write a function named foo that takes two parameters x and y. If y is positive, add all integers from 0 to y-1 to x and return the result. If y is not positive, multiply x by all integers from 0 to |y|-1 and return the result. The function should not use any additional space that scales with the input size. Analyze the time and space complexity of the function.
"""

def foo(x, y):
    if y > 0:
        for i in range(y):
            x += i
    else:
        for i in range(abs(y)):
            x *= i
    return x