"""
QUESTION:
Create a function called `get_unique_odd_numbers` that takes a list of integers as input and returns a new list containing only the unique odd numbers from the input list. The function should not use any built-in functions or libraries to remove duplicates, and its time complexity should be O(nlogn) or less.
"""

def get_unique_odd_numbers(numbers):
    odd_numbers = []
    seen = set()
    for num in numbers:
        if num % 2 != 0 and num not in seen:
            odd_numbers.append(num)
            seen.add(num)
    return odd_numbers