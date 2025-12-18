"""
QUESTION:
Create a function `remove_duplicates` that takes an array and returns the array with all duplicate values removed. The function should have a time complexity of O(n), where n is the length of the array, and should not use any additional data structures other than a set, which is allowed for the purpose of this question.
"""

def remove_duplicates(array):
    unique_array = []
    unique_set = set()
    for num in array:
        if num not in unique_set:
            unique_array.append(num)
            unique_set.add(num)
    return unique_array