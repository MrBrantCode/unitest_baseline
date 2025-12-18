"""
QUESTION:
Write a function named `count_occurrences` that takes a list of integers (`lst`) and a target integer (`value`) as input. Without using any built-in functions or libraries, implement a logic to return the number of occurrences of `value` in `lst`.
"""

def count_occurrences(lst, value):
    count = 0
    for num in lst:
        if num == value:
            count += 1
    return count