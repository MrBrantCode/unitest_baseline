"""
QUESTION:
Write a function named `find_two_largest` that takes a list of integers as input and returns a tuple containing the two largest numbers in the list. The function should not use built-in max or sorting functions.
"""

def find_two_largest(lst):
    max1 = 0
    max2 = 0
    for val in lst:
        if val > max1:
            max2 = max1
            max1 = val
        elif val > max2 and val != max1:
            max2 = val
    return (max1, max2)