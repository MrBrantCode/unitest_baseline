"""
QUESTION:
Write a function `nth_maximum` that takes a list of integers `lst` and an integer `n` as input, and returns the nth maximum value in the list. The function should handle edge cases such as duplicate values and negative integers, and it should not use built-in sorting functions. The function should return `None` if `n` is out of bounds.
"""

def nth_maximum(lst, n):
    # Handle if n is out of bounds
    if n > len(lst) or n < 1:
        return None

    # Bubble sort in descending order
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):

            # Swap if the element found is greater than the next element
            if lst[j] < lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    # Remove duplicates
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)

    if n <= len(unique_lst):
        return unique_lst[n - 1]
    else:
        return None