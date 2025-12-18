"""
QUESTION:
Write a function named `even_elements` that takes a list of integers as input and returns a list of unique even integers greater than 10 and less than 50 in descending order.
"""

def even_elements(lst):
    return sorted(set([element for element in lst if element % 2 == 0 and element > 10 and element < 50]), reverse=True)