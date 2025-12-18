"""
QUESTION:
Write a function `find_duplicates_and_remove` that takes a list of positive integers as input and prints the duplicate elements while removing any duplicates from the original list. The function should have a time complexity of O(n), a space complexity of O(1), and should not use any built-in functions or libraries for duplicate detection or removal. The function should handle edge cases such as an empty list, a list with only one element, and a list with all duplicate elements.
"""

def find_duplicates_and_remove(lst):
    # Edge case: Empty list or list with only one element
    if len(lst) <= 1:
        return []

    duplicates = []
    idx = 0

    while idx < len(lst):
        num = lst[idx]

        # Check if the current number is a duplicate
        if num in duplicates:
            # Remove the duplicate from the list
            lst.pop(idx)
        elif lst.count(num) > 1:
            # Add the number to the duplicates list
            duplicates.append(num)
            # Remove all instances of the number from the list
            while num in lst:
                lst.remove(num)
        else:
            idx += 1

    return duplicates