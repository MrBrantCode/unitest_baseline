"""
QUESTION:
Create a function `remove_duplicates` that takes an array as input and returns the array with duplicates removed. The function should have a time complexity of O(n), where n is the length of the array, and should not use any additional data structures beyond what is strictly necessary. If the array contains duplicate values, the function should remove the duplicates and return the modified array.
"""

def remove_duplicates(array):
    unique_array = []
    unique_set = set()
    for num in array:
        if num not in unique_set:
            unique_array.append(num)
            unique_set.add(num)
    return unique_array