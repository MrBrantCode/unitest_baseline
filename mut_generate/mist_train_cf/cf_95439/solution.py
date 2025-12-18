"""
QUESTION:
Create a function `get_positive_integers` that takes a list of integers as input and returns a new list containing only the positive integers from the input list. The function should have a time complexity of O(n), not use any built-in sorting functions or libraries, and return the resulting list in ascending order.
"""

def get_positive_integers(input_list):
    positive_list = []
    
    for num in input_list:
        if num > 0:
            positive_list.append(num)
    
    positive_list.sort()
    return positive_list