"""
QUESTION:
Write a function `list_sum` that takes a dynamic list of integers as input and returns the sum of all the integers in the list. The input list can contain any number of integers.
"""

def list_sum(num_list):
    total = 0
    for num in num_list:
        total += num
    return total