"""
QUESTION:
Implement a function `custom_sort(arr)` that takes an array of dictionaries as input, where each dictionary contains keys 'name' and 'popularity'. The function should sort the array in the following order: 
- Dictionaries with 'popularity' greater than or equal to 5 should be placed before dictionaries with 'popularity' less than 5.
- Within each of these two groups, the dictionaries should be sorted in descending order of 'popularity'.
- If two dictionaries have the same 'popularity' value, they should be sorted in ascending order of 'name'.
The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def custom_sort(arr):
    return sorted(arr, key=lambda x: (x['popularity'] < 5, -x['popularity'], x['name']))