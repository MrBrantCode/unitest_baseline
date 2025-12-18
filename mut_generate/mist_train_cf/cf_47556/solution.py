"""
QUESTION:
Create a function called `calculate_total` that takes a nested list as input and returns the sum of all integers in the list. The list can contain other data types and nested lists up to a depth of 5, which should be ignored or handled accordingly.
"""

def calculate_total(my_list):
    total = 0
    for item in my_list:
        if type(item) == list:       
            total += calculate_total(item)
        elif type(item) == int:      
            total += item
    return total