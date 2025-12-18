"""
QUESTION:
Write a function `process_numbers` that takes a list of numbers and a boolean as input. If the boolean is True, return a dictionary with numbers from the list as keys and the cumulative sum of their indices as values. If the boolean is False, return a dictionary with numbers from the list as keys and their frequencies as values.
"""

def process_numbers(lst, accumulate_indices):
    result = {}
    for i, num in enumerate(lst):
        if num not in result:
            result[num] = 0
        if accumulate_indices:
            result[num] += i
        else:
            result[num] += 1
    return result