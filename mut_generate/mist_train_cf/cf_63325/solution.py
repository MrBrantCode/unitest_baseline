"""
QUESTION:
Write a function `average_even_ordinal_numbers` that takes a list of integers as input and returns the average value of even ordinal numbers (0-indexed) in the list. The function should handle exceptions for empty lists and lists with no even ordinal numbers, returning an error message in such cases. The solution should have a time complexity of O(n), where n is the number of elements in the list.
"""

def average_even_ordinal_numbers(arr):
    if len(arr) == 0:
        return "Error: List is empty."

    even_ordinal_nums = [arr[i] for i in range(1, len(arr), 2)] 
   
    if len(even_ordinal_nums) == 0:
        return "Error: There are no even ordinal numbers in the list."

    return sum(even_ordinal_nums) / len(even_ordinal_nums)