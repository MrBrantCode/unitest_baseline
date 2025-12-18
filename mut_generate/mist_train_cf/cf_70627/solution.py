"""
QUESTION:
Develop a function called `parity_analyzer` that takes an integer `n` as input and returns a string indicating whether the number is "Even" or "Odd". The function should determine the parity based on the remainder when `n` is divided by 2.
"""

def parity_analyzer(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"