"""
QUESTION:
Write a function `get_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers from the input list, in ascending order.
"""

def get_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    even_numbers.sort()
    return even_numbers