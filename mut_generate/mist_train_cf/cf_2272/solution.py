"""
QUESTION:
Write a function called `extract_values` that takes a dictionary as input and returns a list of its values. The returned list should only include values that are greater than 5 and less than 9. The values in the list should be in ascending order. The function should have a time complexity of O(nlogn), where n is the total number of values in the dictionary.
"""

def extract_values(dictionary):
    filtered_values = [value for value in dictionary.values() if 5 < value < 9]
    sorted_values = sorted(filtered_values)
    return sorted_values