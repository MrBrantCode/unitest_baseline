"""
QUESTION:
Write a function called `count_elements` that takes a list as input and returns the total number of elements in the list without using the `len()` function or the `count()` function. The function should use a for loop to iterate over the elements of the list and count them.
"""

def count_elements(lst):
    count = 0
    for element in lst:
        count += 1
    return count