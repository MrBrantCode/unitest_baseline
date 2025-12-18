"""
QUESTION:
Create a function `remove_duplicates(arr)` that takes a list `arr` as input, modifies it in-place to remove duplicates, and returns the number of unique elements remaining in the list. The function should work for lists containing integers and strings, have a time complexity of O(n) and space complexity of O(n), where n is the number of elements in the list, and maintain the order of the original list.
"""

def remove_duplicates(arr):
    unique_elements = []
    unique_count = 0
    seen_elements = set()

    for element in arr:
        if element not in seen_elements:
            seen_elements.add(element)
            unique_elements.append(element)
            unique_count += 1

    arr.clear()
    arr.extend(unique_elements)
    return unique_count