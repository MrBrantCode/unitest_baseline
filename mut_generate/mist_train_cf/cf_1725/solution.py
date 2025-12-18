"""
QUESTION:
Implement the function `remove_duplicates(lst)` that removes all duplicate elements from the given list `lst` in-place and returns the number of unique elements remaining. The function should maintain the original order of elements, have a time complexity of O(n), and space complexity of O(1), where n is the number of elements in the list. The list can contain both integers and strings.
"""

def remove_duplicates(lst):
    if not lst:
        return 0

    # Maintain a pointer to the last unique element found
    last_unique_index = 0

    # Iterate through the list starting from the second element
    for i in range(1, len(lst)):
        # Check if the current element is different from the last unique element
        if lst[i] != lst[last_unique_index]:
            last_unique_index += 1
            lst[last_unique_index] = lst[i]

    # Return the number of unique elements remaining
    return last_unique_index + 1