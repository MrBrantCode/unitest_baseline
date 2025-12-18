"""
QUESTION:
Implement a function named `unique` that takes a list as input and returns a new list with duplicate elements removed while maintaining the original order of elements. The function should handle empty input lists correctly.
"""

def unique(input_list):
    seen = set()
    output_list = []
    for item in input_list:
        if item not in seen:
            output_list.append(item)
            seen.add(item)
    return output_list