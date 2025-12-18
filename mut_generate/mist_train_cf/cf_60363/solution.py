"""
QUESTION:
Create a function called `even_numbers` that takes a list of integers as input and returns a generator that yields even numbers from the input list. Refactor the function into an equivalent generator expression that is efficient, readable, and Pythonic.
"""

def even_numbers(data_list):
    """Yield even numbers from the input list"""
    return (x for x in data_list if x % 2 == 0)