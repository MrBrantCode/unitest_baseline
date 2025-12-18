"""
QUESTION:
Write a function `find_duplicates` that takes an array of elements as input and identifies all duplicate elements, counting the number of occurrences for each. The function must have a time complexity of O(n), where n is the size of the input array, and must not use any built-in functions or data structures.
"""

def find_duplicates(arr):
    duplicates = {}
    count = {}

    # Loop through the input list
    for element in arr:
        if element in duplicates:
            count[element] += 1
        else:
            duplicates[element] = True
            count[element] = 1

    # Create a dictionary of duplicate elements and their occurrences
    duplicate_elements = {element: occurrences for element, occurrences in count.items() if occurrences > 1}
    return duplicate_elements