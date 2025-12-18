"""
QUESTION:
Design a function named `perfect_numbers` that takes an integer `n` as input and returns a list of all perfect numbers between 1 and `n` (inclusive). A perfect number is a positive integer that is equal to the sum of its positive divisors excluding the number itself.
"""

def perfect_numbers(n):
    result = []
    for i in range(1, n+1):
        sum = 0
        for j in range(1, i):
           if(i % j == 0):
               sum = sum + j
        if (sum == i):
            result.append(i)
    return result