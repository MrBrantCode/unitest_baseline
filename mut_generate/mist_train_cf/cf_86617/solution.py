"""
QUESTION:
Write a function named `find_non_unique_elements` that takes a list of integers as input and returns a list of non-unique elements in ascending order based on their frequency count. If multiple elements have the same frequency count, they should be sorted in ascending order based on their original order in the given list. The function should have a time complexity of O(n^2) and should not use any built-in functions or libraries. The input list can contain integers ranging from -10^6 to 10^6 and can have up to 10^5 elements.
"""

def find_non_unique_elements(lst):
    frequency_count = {}
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count += 1
        frequency_count[lst[i]] = count

    non_unique_elements = [element for element in lst if frequency_count[element] > 1]
    non_unique_elements.sort(key=lambda x: (frequency_count[x], lst.index(x)))
    return non_unique_elements