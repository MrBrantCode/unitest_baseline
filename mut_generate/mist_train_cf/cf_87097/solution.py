"""
QUESTION:
Create a function named `remove_duplicates` that takes a list `lst` as input, where `lst` can contain both integers and strings, and returns the number of unique elements in the list. The function should remove duplicates from the list in-place while maintaining the original order, and it should not use any built-in library functions or data structures. The time complexity of the function should be O(n) and the space complexity should be O(1), where n is the number of elements in the list.
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