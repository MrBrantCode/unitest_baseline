"""
QUESTION:
Write a function named gcd that takes two integers m and n as input and returns their highest common factor (also known as the greatest common divisor). The function should be able to handle any two integers.
"""

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m