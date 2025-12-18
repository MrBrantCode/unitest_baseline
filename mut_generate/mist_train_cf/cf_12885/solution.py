"""
QUESTION:
Implement a function `filter_odd_numbers` that takes a list of integers as input, filters out the odd numbers, and returns a new list containing the odd numbers. The function should have a time complexity of O(n) and a space complexity of O(1), excluding the space required to store the filtered numbers in the new list.
"""

def filter_odd_numbers(input_list):
    filtered_list = []
    for number in input_list:
        if number % 2 != 0:
            filtered_list.append(number)
    return filtered_list