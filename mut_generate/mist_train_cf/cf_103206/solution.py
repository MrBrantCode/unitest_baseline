"""
QUESTION:
Write a function `find_smallest_common_multiple(x, y)` that takes two integers `x` and `y` and returns their smallest common multiple. If either `x` or `y` is zero, return -1, indicating no common multiple exists.
"""

def find_smallest_common_multiple(x, y):
    if x == 0 or y == 0:
        return -1
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    product = x * y
    gcd_value = gcd(x, y)
    smallest_common_multiple = product // gcd_value
    
    return smallest_common_multiple