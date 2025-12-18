"""
QUESTION:
Write a function `compare` that takes two integers `a` and `b` as input and returns an integer value indicating their relative order. The function should use bitwise operators or a single expression to determine the result. If `a` is greater than `b`, the function should print "a is greater than b" and if `b` is greater than `a`, it should print "b is greater than a". If `a` equals `b`, either print statement is acceptable.
"""

def compare(a, b):
    result = (a > b) - (a < b)
    if result > 0:
        print("a is greater than b")
        return 1
    elif result < 0:
        print("b is greater than a")
        return -1
    else:
        print("a is greater than b")  # or print("b is greater than a")
        return 0