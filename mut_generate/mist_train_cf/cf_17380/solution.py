"""
QUESTION:
Create a function `extract_even_numbers` that takes a list of integers as input and returns a new list containing all even numbers that are not divisible by 3. The resulting list should be sorted in descending order. Implement the solution using a single line of code with list comprehension and handle the case where the input list is empty.
"""

def extract_even_numbers(numbers):
    """Returns a new list containing all even numbers not divisible by 3 from the input list, sorted in descending order."""
    return sorted([x for x in numbers if x % 2 == 0 and x % 3 != 0], reverse=True)