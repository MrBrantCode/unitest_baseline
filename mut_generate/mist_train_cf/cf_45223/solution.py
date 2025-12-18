"""
QUESTION:
Write a function called `transcendent_even_quotient(x, y, z)` that takes three non-negative integers x, y, and z as input, and returns the largest even integer within the interval [x, y] that divides perfectly by z. If no such number exists, return -1.
"""

def transcendent_even_quotient(x, y, z):
    for i in range(y, x - 1, -1):  
        if i % z == 0 and i % 2 == 0:  
            return i  
    return -1 