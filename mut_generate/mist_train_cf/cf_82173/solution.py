"""
QUESTION:
Create a function `calculate_frequency` that calculates and returns the prime factors and their frequency for a given number `n`. The function should be able to handle numbers up to 10^9 and should return a dictionary where keys are prime factors and values are their frequencies.
"""

import math

def calculate_frequency(n):
    result = dict()
    while n % 2 == 0:
        if 2 in result:
            result[2] += 1
        else:
            result[2] = 1
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):            
        while n % i== 0:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
            n = n / i

    if n > 2:
        result[n] = 1
            
    return result