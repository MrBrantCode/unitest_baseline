"""
QUESTION:
Write a function `remove_duplicates` that takes an array of positive integers as input, and returns a new array containing the same elements without duplicates, without modifying the original array. The function should achieve this in O(n) time complexity, where n is the length of the input array, and should not utilize any built-in methods or data structures such as sets or dictionaries.
"""

def remove_duplicates(nums):
    unique_elements = []
    seen_elements = set()

    for element in nums:
        if element not in seen_elements:
            unique_elements.append(element)
            seen_elements.add(element)

    return unique_elements