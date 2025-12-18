"""
QUESTION:
Compute the sum of all elements in a nested list. Implement a function `nested_list_sum(nested_list)` that takes a list containing integers and/or nested lists of integers as input and returns the total sum of all integers in the list. The function should recursively traverse the nested lists to include all integers in the sum.
"""

def nested_list_sum(nested_list):
    total = 0
    for element in nested_list:
        if type(element) == list:
            total += nested_list_sum(element)
        else:
            total += element
    return total