"""
QUESTION:
Write a function `reverse_difference` that takes a positive integer less than 10^18 as input and returns the absolute difference between the number and its reverse as an integer. The solution should have a time complexity of O(logN), where N is the given number.
"""

def reverse_difference(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    reversed_num = int(reversed_str)
    return abs(num - reversed_num)