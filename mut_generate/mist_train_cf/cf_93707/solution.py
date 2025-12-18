"""
QUESTION:
Create a function called `remove_duplicates` that takes an array as input and returns an array containing only unique values. The function should have a time complexity of O(n), where n is the length of the input array, and should not use any additional data structures besides the input array and a set. The function should modify the input array by removing duplicates and return the modified array.
"""

def remove_duplicates(arr):
    unique_values = set()
    result = []
    for num in arr:
        if num not in unique_values:
            unique_values.add(num)
            result.append(num)
    return result