"""
QUESTION:
Create a recursive function called 'power' that takes two parameters: the base number 'n' and the exponent 'm'. The function should return the value of 'n' raised to the power of 'm', handling both positive and negative exponents.
"""

def power(n, m):
    if m == 0:
        return 1
    elif m < 0:
        return 1 / power(n, -m)
    else:
        return n * power(n, m - 1)