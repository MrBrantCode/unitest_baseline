"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of strings as input and returns a new list with all duplicates removed while maintaining the original order of the elements. The function must have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list. The function must not use any built-in functions or methods that directly remove duplicates or any additional data structures other than the input list itself.
"""

def remove_duplicates(lst):
    seen = set()
    result = []
    for element in lst:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result