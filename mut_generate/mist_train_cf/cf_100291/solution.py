"""
QUESTION:
Create a function called `square_dict` that takes a list of integers as input and returns a dictionary where the keys are the original numbers and the values are their corresponding squares.
"""

def square_dict(input_list):
    result_dict = {}
    for num in input_list:
        result_dict[num] = num ** 2
    return result_dict