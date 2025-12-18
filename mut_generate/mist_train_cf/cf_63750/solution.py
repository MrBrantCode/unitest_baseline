"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input, converts it to a tuple, and removes all duplicates without altering the order of elements while preserving the integrity of data sequence and case-sensitivity. The function should return a tuple. The input list can contain a mix of data types, including integers and strings.
"""

def remove_duplicates(input_list):
    final_list = []
    for num in input_list:
        if num not in final_list:
            final_list.append(num)
    return tuple(final_list)