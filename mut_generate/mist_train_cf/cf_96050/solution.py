"""
QUESTION:
Write a function `get_unique_strings` that takes a list of strings as input and returns a list of unique strings, maintaining the original order. The input list can contain up to 1 million elements. The function should have a time complexity of O(n), where n is the number of elements in the input list, to ensure efficient performance.
"""

def get_unique_strings(input_list):
    unique_set = set()
    unique_list = []

    for string in input_list:
        if string not in unique_set:
            unique_set.add(string)
            unique_list.append(string)

    return unique_list