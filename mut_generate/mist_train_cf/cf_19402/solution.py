"""
QUESTION:
Create a function `sum_of_odd_numbers` that takes a positive integer `n` as input. The function should return the sum of all odd numbers from 1 to `n` multiplied by 3. If `n` is a negative number, the function should return an error message stating that only positive numbers are allowed.
"""

def sum_of_odd_numbers(n):
    if n < 1:
        return "Error: Only positive numbers are allowed."
    
    sum_of_odds = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            sum_of_odds += i
    
    return sum_of_odds * 3