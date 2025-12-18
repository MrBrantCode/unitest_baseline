"""
QUESTION:
Design a function `get_maximum_number()` that takes user input for a list of numbers and prints the maximum among them. The function should handle both positive and negative numbers, floating-point numbers, invalid or non-numeric values, and cases where the user inputs an empty list of numbers or a single number. The function should have a time complexity of O(n), where n is the number of elements in the input list, and should also handle cases where the maximum value occurs multiple times in the list and print the index(es) of occurrence.
"""

def get_maximum_number(numbers):
    max_num = float('-inf')
    max_indices = []
    for i, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_indices = [i]
        elif num == max_num:
            max_indices.append(i)
    return max_num, max_indices