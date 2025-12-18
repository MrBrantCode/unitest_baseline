"""
QUESTION:
Find the two maximum numbers in a list of integers. The function should be named `find_max_two_numbers`, take a list of integers as input, and return a list of the two maximum numbers. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of integers in the input list. The input list can contain both positive and negative integers, and the numbers can be repeated.
"""

def find_max_two_numbers(arr):
    max1 = float('-inf')
    max2 = float('-inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num < max1 and num > max2:
            max2 = num

    return [max1, max2]