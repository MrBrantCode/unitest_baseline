"""
QUESTION:
Develop a function named `remove_sequential_duplicates` that takes a list containing strings and integers as input, removes sequential duplicates, and returns the modified list while preserving the original order. The function should handle lists where the first element may also be a duplicate.
"""

def remove_sequential_duplicates(input_list):
    result = []
    for i in range(len(input_list)):
        if i == 0 or input_list[i] != input_list[i - 1]:
            result.append(input_list[i])
    return result