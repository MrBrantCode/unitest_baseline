"""
QUESTION:
Write a function `count_occurrences` that takes a list of integers and a target integer as input and returns the number of occurrences of the target integer in the list. The function should not use built-in functions or methods that directly count the occurrences of the target integer in the list.
"""

def count_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count