"""
QUESTION:
Create a function named `remove_duplicates` that takes an array as input and returns the array with all duplicate values removed. The function should have a time complexity of O(n), where n is the length of the array, and cannot use any additional data structures with a space complexity greater than O(n).
"""

def remove_duplicates(arr):
    unique_values = set()
    result = []
    for num in arr:
        if num not in unique_values:
            unique_values.add(num)
            result.append(num)
    return result