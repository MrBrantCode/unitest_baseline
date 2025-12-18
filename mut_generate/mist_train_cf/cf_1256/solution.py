"""
QUESTION:
Find the most common elements across two sets of data, where each element can only appear once in the final result. Implement a function named `find_common_elements` that takes two sets as input and returns a set of common elements between the two input sets. The function must have a time complexity of O(n), where n is the total number of elements in both sets combined, and a space complexity of O(1), without using any additional data structures (such as arrays or sets) and only modifying the original sets if necessary.
"""

def find_common_elements(set1, set2):
    for num in set1.copy():
        if num not in set2:
            set1.remove(num)
    return set1