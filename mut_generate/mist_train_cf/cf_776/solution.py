"""
QUESTION:
Create a function called `filter_and_sort_array` that takes an array of objects as input. The function should filter the array to include only objects with a 'value' property that is a number greater than 5 and a 'type' property equal to 'string'. The function should return the filtered array sorted in descending order based on the 'value' property. If the 'value' property is missing or not a number, the object should be excluded from the output. The function should be implemented in a single line of code.
"""

def filter_and_sort_array(array):
    return sorted([obj for obj in array if 'value' in obj and isinstance(obj['value'], (int, float)) and obj['value'] > 5 and obj['type'] == 'string'], key=lambda x: x['value'], reverse=True)