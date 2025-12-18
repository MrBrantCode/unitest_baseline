"""
QUESTION:
Implement a function called `calculate_value` that takes a list of tuples as input where each tuple contains two elements. The function should multiply the first element of each tuple by the second element, sum up all the products, and return the final result. The input list can contain any number of tuples with numeric elements.
"""

def calculate_value(input_list):
    return sum(i[0] * i[1] for i in input_list)