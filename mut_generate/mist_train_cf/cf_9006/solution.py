"""
QUESTION:
Write a function called `count_occurrences` that takes a list of integers and a target integer value as input, and returns the number of occurrences of the target value in the list.
"""

def count_occurrences(lst, value):
    count = 0
    for num in lst:
        if num == value:
            count += 1
    return count