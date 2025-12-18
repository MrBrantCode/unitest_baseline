"""
QUESTION:
Create a function named `find_occurrences` that takes a list of numbers and a target number as input. The function should return the index of the first occurrence and the index of the last occurrence of the target number in the list. If the target number is not present in the list, the function should return -1 for both indices.
"""

def find_occurrences(lst, num):
    try:
        first_index = lst.index(num)
        last_index = len(lst) - lst[::-1].index(num) - 1
        return first_index, last_index
    except ValueError:
        return -1, -1