"""
QUESTION:
Create a function called `get_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers. The function should have a time complexity of O(n), where n is the length of the input list, and should not use any built-in functions or libraries.
"""

def get_even_numbers(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers