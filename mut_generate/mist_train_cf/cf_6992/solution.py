"""
QUESTION:
Write a function `get_largest_sum` that takes a list of integers `num_list` as input and returns the largest sum of any two numbers in the list. The length of `num_list` is between 2 and 10^6, and each element is an integer between -10^9 and 10^9.
"""

def get_largest_sum(num_list):
    # Sort the list in descending order
    num_list.sort(reverse=True)
    # Return the sum of the two largest numbers in the list
    return num_list[0] + num_list[1]