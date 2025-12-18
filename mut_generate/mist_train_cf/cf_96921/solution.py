"""
QUESTION:
Create a function `get_unique_list` that generates a list of unique integers from a given list of integers, maintaining the order of the first occurrence of each integer, without using any built-in functions or libraries. The function should take a list of integers as input and return a list of unique integers.
"""

def get_unique_list(input_list):
    unique_list = []
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list