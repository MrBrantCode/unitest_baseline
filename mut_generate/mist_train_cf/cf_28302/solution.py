"""
QUESTION:
Implement a function `all_to_dec(z, p)` that takes a string `z` representing a number in base `p` and an integer `p` as input, and returns a tuple containing the decimal equivalent of `z` and a string showing the step-by-step conversion process. The function should iterate through the digits of `z` and calculate the decimal equivalent using the base `p` representation. The base `p` is between 2 and 36, and the digits in `z` can be both numeric and alphabetic (e.g., 'A' represents the number 10 in base 16).
"""

def all_to_dec(z, p):
    n = 0
    s = ''
    for i in range(len(z)):
        n += int(z[len(z) - (i + 1)], p) * (p ** i)
        s += str(int(z[len(z) - (i + 1)], p)) + '*' + str(p ** i) + ' + '
    s = s[:-3] + ' = ' + str(n)
    return n, s