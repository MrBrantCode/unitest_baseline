"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of numbers as input, sorts them in ascending order of absolute values, and returns a new list with duplicates removed. If there are multiple numbers with the same absolute value, they should be sorted in descending order. The function should handle empty or single-element input lists.
"""

def remove_duplicates(numbers):
    sorted_numbers = sorted(numbers)
    result = []
    for number in sorted_numbers:
        if number not in result:
            result.append(number)
    
    return sorted(result, key=lambda x: (abs(x), -x))