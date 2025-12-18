"""
QUESTION:
Create a function named `sorted_list` that takes a list of integers as input. The function should sort the list in ascending order, remove duplicates, and then reorganize the list such that even numbers come first, followed by negative numbers, and then odd numbers, all in ascending order. The function should also return two additional values: the largest negative integer from the original list (or 0 if no negative integers exist), and the smallest positive integer from the sorted and deduplicated list (or 0 if no positive integers exist).
"""

def sorted_list(lst):
    lst = sorted(set(lst))
    evens = sorted([num for num in lst if num >= 0 and num % 2 == 0])
    negs = sorted([num for num in lst if num < 0])
    odds = sorted([num for num in lst if num > 0 and num % 2 != 0])

    sorted_lst = evens + negs + odds
    largest_negative = max(negs) if negs else 0
    smallest_positive = min([num for num in lst if num > 0]) if any(num > 0 for num in lst) else 0

    return sorted_lst, largest_negative, smallest_positive