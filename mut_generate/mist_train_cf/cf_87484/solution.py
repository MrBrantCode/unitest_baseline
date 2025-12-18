"""
QUESTION:
Create a function `custom_sort` that sorts an array of dictionaries based on the following conditions:

- Dictionaries with a 'popularity' value of less than 5 are placed at the end of the sorted array.
- Dictionaries are sorted by the 'popularity' value in descending order.
- If two dictionaries have the same 'popularity' value, they are sorted by the 'name' value in ascending order.

Implement the sorting algorithm with a time complexity of O(n log n) and a space complexity of O(n).
"""

def custom_sort(arr):
    return sorted(arr, key=lambda x: (x['popularity'] < 5, -x['popularity'], x['name']))