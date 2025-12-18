"""
QUESTION:
Write a function named `compute_gcf` that takes two integers `x` and `y` as input and returns their greatest common factor (GCF). The function should find the largest number that divides both `x` and `y` without leaving a remainder.
"""

def compute_gcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i 
    return gcf