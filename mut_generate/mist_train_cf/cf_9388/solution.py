"""
QUESTION:
Write a function `sum_of_odd_numbers(n)` that calculates the sum of the first `n` odd numbers, excluding any number divisible by 3. The function should not take any other parameters and return the calculated sum.
"""

def sum_of_odd_numbers(n):
    count = 0
    sum = 0
    number = 1

    while count < n:
        if number % 3 != 0:
            sum += number
            count += 1
        number += 2  

    return sum