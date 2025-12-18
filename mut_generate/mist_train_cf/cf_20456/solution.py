"""
QUESTION:
Write a function that uses the filter() function to find all even numbers in a given range and returns them in a list sorted in descending order. The function should be named get_even_numbers and take one argument: an integer representing the end of the range (starting from 0).
"""

def get_even_numbers(end):
    return sorted(filter(lambda x: x % 2 == 0, range(end+1)), reverse=True)