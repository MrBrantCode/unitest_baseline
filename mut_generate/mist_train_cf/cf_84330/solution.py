"""
QUESTION:
Write a recursive function `compute_product` that calculates the product of all integers in a list. The function should take a list of integers and an optional index parameter (defaulting to 0) as input. The list of integers should be dynamically generated based on user input, where the user specifies the number of integers 'n' and then provides each integer individually. The function should handle cases where the index equals the length of the list, and it should return the product of all integers in the list.
"""

def compute_product(num_list, index=0):
    if index == len(num_list):
        return 1
    else:
        return num_list[index] * compute_product(num_list, index + 1)