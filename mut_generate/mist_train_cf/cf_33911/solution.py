"""
QUESTION:
Create a function `sum_odd_multiples_of_three` that takes two integers `start` and `end` as input and returns the sum of all odd numbers between `start` and `end` (inclusive) that are multiples of three. The input integers are restricted to the range 1 <= start <= end <= 10^6.
"""

def sum_odd_multiples_of_three(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 != 0 and num % 3 == 0:
            total_sum += num
    return total_sum