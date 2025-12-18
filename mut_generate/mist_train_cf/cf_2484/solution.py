"""
QUESTION:
Write a function named `extract_even_numbers` that takes a list of integers as input, extracts all the even numbers that are not divisible by 3, and returns the resulting list sorted in descending order. The solution must be implemented in a single line of code using list comprehension, a lambda function, the map() function, and the sorted() function.
"""

def extract_even_numbers(lst):
    return sorted(list(filter(lambda x: x % 2 == 0 and x % 3 != 0, lst)), reverse=True)