"""
QUESTION:
Design a function named `separate_numbers` that takes a list of numbers as input and returns two lists: one containing even numbers and the other containing odd numbers. The function should use list comprehension and eliminate any duplicate numbers using a set data structure.
"""

def separate_numbers(number_list):
    even_numbers = list(set(num for num in number_list if num % 2 == 0))
    odd_numbers = list(set(num for num in number_list if num % 2 != 0))

    return even_numbers, odd_numbers