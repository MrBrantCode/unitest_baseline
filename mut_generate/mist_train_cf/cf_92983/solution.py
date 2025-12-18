"""
QUESTION:
Create a function called `sum_of_multiples(num)` that calculates the sum of all multiples of 4 and 6 up to the given number `num`. The function should return the sum of these multiples.
"""

def sum_of_multiples(num):
    sum = 0
    for i in range(1, num + 1):
        if i % 4 == 0 or i % 6 == 0:
            sum += i
    return sum