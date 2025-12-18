"""
QUESTION:
Write a function `most_occurring_divisible_by_3_and_5` that takes a list of integers as input and returns the most occurring item that is divisible by both 3 and 5. If no such item exists, return None. The function should handle any list of integers as input.
"""

def most_occurring_divisible_by_3_and_5(input_list):
    count_dict = {}
    for item in input_list:
        if item % 3 == 0 and item % 5 == 0:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
    return max(count_dict, key=count_dict.get) if count_dict else None