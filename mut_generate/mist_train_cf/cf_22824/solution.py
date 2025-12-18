"""
QUESTION:
Create a function `count_ways(n)` to calculate the number of different ways to climb n stairs with the constraint that you can only climb 1, 2, or 3 stairs at a time. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def count_ways(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    
    a, b, c = 1, 1, 2
    for i in range(3, n+1):
        total = a + b + c
        a, b, c = b, c, total
    
    return c