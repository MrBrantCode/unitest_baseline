"""
QUESTION:
Create a function `remove_duplicates` that takes a list of numbers as input, removes duplicates, and returns a new list sorted in ascending order of absolute values. If multiple numbers have the same absolute value, they should be sorted in descending order. The function should handle cases where the input list is empty or contains only one element.
"""

def remove_duplicates(numbers):
    sorted_numbers = sorted(numbers)
    result = []
    for number in sorted_numbers:
        if number not in result:
            result.append(number)
    
    return sorted(result, key=lambda x: (abs(x), -x))