"""
QUESTION:
Write a function named `sum_even_numbers` that calculates the sum of all even numbers less than or equal to a given number `n`. The function should use a loop to iterate through numbers from 1 to `n` and include a conditional statement to check if a number is even before adding it to the sum. The time complexity should be O(n).
"""

def sum_even_numbers(n):
    """
    Calculates the sum of all even numbers less than or equal to n.
    """
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i
    return total