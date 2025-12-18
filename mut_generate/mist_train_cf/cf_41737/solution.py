"""
QUESTION:
Write a function `count_good_kids(behavior)` that takes a list of strings as input, where each string consists of characters 'G' (good kid) and 'V' (naughty kid), and returns a list of integers representing the count of good kids for each day. Each integer in the output list should correspond to the count of 'G's in the corresponding input string.
"""

def count_good_kids(behavior):
    return [day.count("G") for day in behavior]