"""
QUESTION:
Write a function called `sort_even` that takes a list of integers as input. The function should maintain the elements at odd indices in their original positions, while sorting the elements at even indices in descending order. For negative even-indexed integers, they should be sorted in descending order separately from non-negative integers. The function should return a new list with the described properties.
"""

def sort_even(l: list):
    # Separate even- and odd-indexed elements
    even_elements = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_elements = [x for i, x in enumerate(l) if i % 2 == 1]

    # Sort even_index elements
    negative_even = sorted([x for x in even_elements if x < 0], reverse=True)
    non_negative_even = sorted([x for x in even_elements if x >= 0], reverse=True)
    even_elements = negative_even + non_negative_even

    # Reintegrate even_index elements
    new_l = []
    for i, x in enumerate(l):
        if i % 2 == 0:
            new_l.append(even_elements.pop(0))
        else:
            new_l.append(x)

    return new_l