"""
QUESTION:
Create a function `remove_items` that takes a list `lst` and an item as input, and returns the list with all occurrences of the item removed. The function should not use the built-in 'remove' function, 'del' keyword, or any other built-in function specifically designed for removing elements from a list. The function should have a time complexity of O(n), where n is the length of the list.
"""

def remove_items(lst, item):
    i = 0
    while i < len(lst):
        if lst[i] == item:
            # Shift all elements after i to the left
            for j in range(i, len(lst) - 1):
                lst[j] = lst[j + 1]
            lst.pop()  # Remove the last element
        else:
            i += 1

    return lst