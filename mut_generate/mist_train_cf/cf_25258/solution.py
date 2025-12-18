"""
QUESTION:
Create a function named `store_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers from the input list.
"""

def store_odd_numbers(numbers):
    odds = []
    for num in numbers:
        if num % 2 != 0:
            odds.append(num)
    return odds