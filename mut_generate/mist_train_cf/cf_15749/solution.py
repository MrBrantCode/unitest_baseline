"""
QUESTION:
Write a function `sum_of_odd_numbers(n)` that calculates the sum of the first `n` odd numbers, excluding any number that is divisible by both 3 and 5.
"""

def sum_of_odd_numbers(n):
    count = 0
    sum_of_odds = 0
    num = 1
    
    while count < n:
        if num % 3 != 0 or num % 5 != 0:
            sum_of_odds += num
            count += 1
        num += 2
    
    return sum_of_odds