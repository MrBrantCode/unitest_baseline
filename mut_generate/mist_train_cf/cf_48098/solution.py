"""
QUESTION:
Create a function `custom_sort` that sorts a given list of integers in descending order, preserving the relative order of equal elements based on their first appearance in the original list. The function should optimize for computational efficiency to handle large lists. The sorted list should be returned.
"""

def custom_sort(numbers):
    # Create a dictionary to store the index of first occurrence of a number
    index_dict = {v: i for i, v in enumerate(numbers)}

    # Use sorted() function with custom rules
    sorted_nums = sorted(numbers, key=lambda x: (-x, index_dict[x]))

    return sorted_nums