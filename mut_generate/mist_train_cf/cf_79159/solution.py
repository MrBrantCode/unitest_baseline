"""
QUESTION:
Write a function `harmonic_mean` that calculates the harmonic mean of a list of numbers represented as a dictionary where keys are the numbers and values are their frequencies. The function should take a dictionary as input and return the harmonic mean.
"""

def harmonic_mean(dict_num):
    n = 0
    d = 0
    for k,v in dict_num.items():
        n += v
        d += v / k
    return n / d