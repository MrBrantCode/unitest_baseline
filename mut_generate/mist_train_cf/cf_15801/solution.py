"""
QUESTION:
Remove the element "red" from the array and return the remaining elements in alphabetical order (case-sensitive). The array can contain duplicate elements. Implement a function named `remove_and_sort` to solve this problem.
"""

def remove_and_sort(arr):
    result = [element for element in arr if element != "red"]
    result.sort()
    return result