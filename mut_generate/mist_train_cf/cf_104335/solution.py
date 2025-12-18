"""
QUESTION:
Write a function `compare_lists(list1, list2)` that compares two lists of numbers and returns a new list with the common elements and their respective counts. The common elements should be in the same order as they appear in the original lists, and duplicates should be considered separately. The function should return a list of common elements and a list of their counts.
"""

def compare_lists(list1, list2):
    common_elements = []
    count = []

    # Iterate over each element in list1
    for num in list1:
        # Check if the element is also present in list2
        if num in list2:
            # Add the element to the common_elements list
            common_elements.append(num)
            # Count the occurrences of the element in both lists
            count.append(min(list1.count(num), list2.count(num)))

    return common_elements, count