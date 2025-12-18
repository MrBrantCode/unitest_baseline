"""
QUESTION:
Create a function named `filter_numbers` that takes a list of numbers as input and returns a new list containing only the numbers that are even (i.e., remainder when divided by 2 is 0) and not divisible by 5. Do not use built-in filter functions.
"""

def filter_numbers(num_list):
    new_list = []
    for num in num_list:
        if num % 2 == 0 and num % 5 != 0:
            new_list.append(num)
    return new_list