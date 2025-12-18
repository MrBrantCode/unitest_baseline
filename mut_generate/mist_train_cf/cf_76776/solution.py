"""
QUESTION:
Create a function named `get_consecutive_pairs` that takes a list as input and returns a list of tuples, where each tuple contains two consecutive elements from the input list.
"""

def entrance(input_list):
    return list(zip(input_list, input_list[1:]))