"""
QUESTION:
Implement a function named `count_occurrences` that takes in two parameters: an array `arr` and a specific integer `specific_value`. The function should count the number of times `specific_value` exists in `arr`, where the array can contain up to 10^9 elements, each ranging from -10^9 to 10^9, and the function should achieve a time complexity of O(n) or better.
"""

def count_occurrences(arr, specific_value):
    count = 0
    for element in arr:
        if element == specific_value:
            count += 1
    return count