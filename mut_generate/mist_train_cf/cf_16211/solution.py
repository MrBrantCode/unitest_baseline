"""
QUESTION:
Write a function `find_most_occurring_divisible_by_3_and_5(input_list)` that finds the most occurring item from the given list that is divisible by both 3 and 5. If no such item exists, return None. The function should take a list of integers as input and return an integer or None.
"""

def find_most_occurring_divisible_by_3_and_5(input_list):
    filtered_list = [num for num in input_list if num % 3 == 0 and num % 5 == 0]
    if len(filtered_list) == 0:
        return None
    else:
        return max(filtered_list, key=filtered_list.count)