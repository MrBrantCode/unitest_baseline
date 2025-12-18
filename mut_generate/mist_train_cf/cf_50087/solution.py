"""
QUESTION:
Design a function called `perfect_numbers(n)` that takes an integer `n` as input and returns a list of all perfect numbers up to `n`. A perfect number is a number that is equal to the sum of its positive divisors, excluding the number itself.
"""

def perfect_numbers(n):
    perfects = []
    for num in range(1, n):
        sum_list = []
        for i in range(1, num):
            if(num % i == 0):
                sum_list.append(i)
        if(sum(sum_list) == num):
            perfects.append(num)
    return perfects