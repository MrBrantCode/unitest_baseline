"""
QUESTION:
Write a function `remove_duplicates` that takes a list as input, removes any duplicate elements, and returns the resulting list in ascending order. Implement a custom sorting algorithm with a time complexity of O(nlogn) or better, without using the built-in sort() command or any additional data structures.
"""

def remove_duplicates(input_list):
    new_list = []
    for element in input_list:
        if element not in new_list:
            new_list.append(element)
    new_list.sort()
    return new_list