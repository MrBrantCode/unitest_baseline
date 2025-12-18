"""
QUESTION:
Find the smallest possible integer value for the second number such that the least common multiple of the two numbers (one given as 45) divided by their greatest common divisor equals 33.
"""

import math

def entrance(number, quotient):
    i = 1
    while True: 
        gcd = math.gcd(number, i)
        lcm = abs(number*i)//gcd
        if lcm//gcd == quotient:
            return i
        i += 1