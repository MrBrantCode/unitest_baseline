"""
QUESTION:
Create a function named `group_list()` that takes a list of integers as input and returns a dictionary with two keys: 'Even Numbers' and 'Odd Numbers'. The function should group the input list into two partitions: one for even numbers and one for odd numbers, based on the criterion that a number is even if it is divisible by 2 without a remainder.
"""

def group_list(input_list):
    even_numbers = [i for i in input_list if i % 2 == 0]
    odd_numbers = [i for i in input_list if i % 2 != 0]
    
    return {'Even Numbers':even_numbers, 'Odd Numbers':odd_numbers}