"""
QUESTION:
Write a function `reverse_difference(num)` that takes a positive integer `num` less than 10^18 as input and returns the absolute difference between `num` and its reverse as an integer. The function should have a time complexity of O(logN), where N is the given number.
"""

def reverse_difference(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    reversed_num = int(reversed_str)
    return abs(num - reversed_num)