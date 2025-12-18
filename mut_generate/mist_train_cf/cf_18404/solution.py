"""
QUESTION:
Implement a function called `minL` that takes two lists of positive integers as input and returns the smallest element from both lists. The input lists will always contain at least one element and will not exceed 10^6 in length. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the total number of elements in the input lists.
"""

def minL(list1, list2):
    # Initialize the minimum element to the maximum possible value
    min_element = float('inf')

    # Find the length of the longest list
    max_len = max(len(list1), len(list2))

    # Iterate through both lists simultaneously
    for i in range(max_len):
        # Check if the current index is within the bounds of each list
        if i < len(list1):
            min_element = min(min_element, list1[i])
        if i < len(list2):
            min_element = min(min_element, list2[i])

    return min_element