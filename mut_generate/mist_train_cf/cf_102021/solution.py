"""
QUESTION:
Write a function `add(x, y)` that takes two integers `x` and `y` as input and returns their sum plus one. The function must also print all integers from 0 to the sum of `x` and `y`. What is the Big O notation for this algorithm?
"""

def add(x, y):
    sum_xy = x + y
    for i in range(sum_xy + 1):
        print(i)
    return sum_xy + 1