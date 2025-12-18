"""
QUESTION:
Create a function `AdvancedFunction` that takes a list of numbers as input, returns a list of unique numbers less than 50, and handles unexpected input types and non-numeric data. The function should be able to process negative numbers and zeros, and maintain the original order of elements in the output list.
"""

def AdvancedFunction(lst):
    result = set()
    unique_nums = []
    try:
        for num in lst:
            if isinstance(num, (int, float)) and num < 50 and num not in result:
                result.add(num)
                unique_nums.append(num)
        return unique_nums
    except TypeError:
        print("Error: The list should only contain numbers.")