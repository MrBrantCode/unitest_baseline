"""
QUESTION:
Write a function named `search_number` that takes a list of integers and a target integer as input, and returns "Found!" if the target integer is in the list and "Not found." otherwise. The function should use a data structure that allows for fast search. The function should only print the result once, even if the target integer is present multiple times in the list.
"""

def search_number(numbers, target):
    num_set = set(numbers)
    if target in num_set:
        return "Found!"
    else:
        return "Not found."