"""
QUESTION:
Write a function `find_max_unique_numbers` that takes a list of integers as input and returns a list containing the maximum value of each unique number in the input list. The function must achieve this in a single loop with a time complexity of O(n), where n is the length of the input list.
"""

def find_max_unique_numbers(input_list):
    max_values = {}
    
    for num in input_list:
        if num not in max_values:
            max_values[num] = num
        else:
            max_values[num] = max(max_values[num], num)
    
    return list(max_values.values())